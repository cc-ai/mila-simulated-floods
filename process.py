import torch
from skimage.io import imread
import numpy as np

SEG_CLASS_TO_RGBA = {
    0: (0, 0, 255, 255),  # Water
    1: (55, 55, 55, 255),  # Ground
    2: (0, 255, 255, 255),  # Building
    3: (255, 212, 0, 255),  # Traffic items
    4: (0, 255, 0, 255),  # Vegetation
    5: (255, 97, 0, 255),  # Terrain
    6: (255, 0, 0, 255),  # Car
    7: (60, 180, 60, 255),  # Trees
    8: (255, 0, 255, 255),  # Person
    9: (0, 0, 0, 255),  # Sky
    10: (255, 255, 255, 255),  # Default
}

RGBA_TO_SEG_CLASS = {
    rgba_value: class_id for class_id, rgba_value in SEG_CLASS_TO_RGBA.items()
}


def load_unity_depth(unity_depth_path, far=1000):
    """Transforms the 3-channel encoded depth map from our Unity simulator
    to 1-channel depth map containing metric depth values.
    The depth is encoded in the following way:
    - The information from the simulator is (1 - LinearDepth (in [0,1])).
        far corresponds to the furthest distance to the camera included in the
        depth map.
        LinearDepth * far gives the real metric distance to the camera.
    - depth is first divided in 31 slices encoded in R channel with values ranging
        from 0 to 247
    - each slice is divided again in 31 slices, whose value is encoded in G channel
    - each of the G slices is divided into 256 slices, encoded in B channel

    In total, we have a discretization of depth into N = 31*31*256 - 1 possible values,
    covering a range of far/N meters.

    Note that, what we encode here is 1 - LinearDepth so that the furthest point is
    [0,0,0] (that is sky) and the closest point[255,255,255]

    The metric distance associated to a pixel whose depth is (R,G,B) is :
        d = (far/N) * [((255 - R)//8)*256*31 + ((255 - G)//8)*256 + (255 - B)]

    Args:
        unity_depth_tensor (torch.Tensor): one depth map obtained from our simulator
        far (int, optional): [description]. Defaults to 1000.

    Returns:
        [numpy.array]: decoded metric depth with shape (1 x height x width).
    """

    depth_image = imread(unity_depth_path).astype(np.float32)

    R = depth_image[:, :, 0]
    G = depth_image[:, :, 1]
    B = depth_image[:, :, 2]

    R = ((247 - R) / 8).type(torch.IntTensor)
    G = ((247 - G) / 8).type(torch.IntTensor)
    B = (255 - B).type(torch.IntTensor)
    metric_depth = ((R * 256 * 31 + G * 256 + B).type(torch.FloatTensor)) / (
        256 * 31 * 31 - 1
    )
    metric_depth = metric_depth * far

    metric_depth = metric_depth[None, ...]

    return metric_depth


def load_unity_segmap(unity_seg_path):
    """Change a segmentation RGBA array to a segmentation array
                            with each pixel being the index of the class
    Arguments:
        numpy array -- segmented image of size (H) x (W) x (4 RGBA values)
    Returns:
        numpy array of size (1) x (H) x (W) with each pixel being the index of the class
    """
    seg_image = imread(unity_seg_path)
    seg_class_arr = np.zeros((1, seg_image.shape[0], seg_image.shape[1]))

    for i in range(seg_image.shape[0]):
        for j in range(seg_image.shape[1]):
            pixel_rgba = tuple(seg_image[i, j, :])
            if pixel_rgba in RGBA_TO_SEG_CLASS.keys():
                seg_class_arr[0, i, j] = RGBA_TO_SEG_CLASS[pixel_rgba]
            else:
                raise ValueError(f"Unknown RGBA value {pixel_rgba}")
    return seg_class_arr
