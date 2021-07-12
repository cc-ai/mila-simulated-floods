# MILA Simulated Floods Dataset

## Dataset Presentation
MILA Simulated Floods Dataset is a 1.5 square km virtual world using the Unity3D game engine including urban, suburban and rural areas.
The *urban* environment contains skyscrapers, large buildings, and roads, as well as objects such as traffic items and vehicles. The *rural* environment consists of a landscape of grassy hills , forests, and mountains, with sparse houses and other buildings such as a church, and no roads. The rural and urban areas make up for 1 square km of our virtual world. A bird’s eye view of the urban area (city) and rural area(outskirts of the city) of our simulated world is presented below:

![](/image/bird_eye.png)

The *suburban* environment is a residential area of 0.5 square km with many individual houses with front yards. 

![](/image/0001.png)

To gather the simulated dataset, we captured *before* and *after* flood pairs from 2000 viewpoints with the following modalities:
- non-flooded RGB image, depth map, segmentation map
- flooded RGB image, binary mask of the flooded area, segmentation map

The camera was placed about 1.5 above ground, and has a field of view of *120 degree*, and the resolution of the images is *1200 x 900*. At each viewpoint, we took 10 pictures, by varying slightly the position of the camera in order to augment the dataset.

More samples are given as follows:

![](/image/samples.png)

### Depth 
The depth maps are provided as RGB images for the *before* case, and the depth is recorded up to 1000 m away from the camera, with precision of 4 mm. 

### Segmentation
There are nine different classes of objects in the simulated world:
- sky
- ground: road, sidewalks, road markings, anything that is asphalt
- building
- traffic item: lampposts, traffic signs, poles
- vegetation: small bushes, trees, hedges excludes grass, lawns
- terrain: rocks, soil, lawns
- car: cars and trucks
- other: miscellaneous objects such as postboxes, trashcans, garbage bags, etc.
- water: only present in the *after* flooded images
 
Please note that people are not included in the simulated world. The segmentation model is able to learn this class from the real world due to the supervision signal given by the HRNet pseudo-labels.

### Mask
We also include binary masks of the flood (water segmentation) for the *after* images. The masks are used to train the Masker with ground truth target flood masks in the simulated domain.

![](/image/overall.png)
## Usage 
The dataset can be downloaded from [Google Drive](https://drive.google.com/drive/folders/1aU6f-El0Sps7iBMMekEePzzqDXNmwAiv?usp=sharing).

## Dataset File Structure
```
Mila-Simulated-flood-19800-high
└───Mila-Simulated-flood
    └───Unity-19800-high
        └───Depth
            │   0001_high.png
            │   0001_0_high.png
            │   0001_1_high.png
            │   ...
            │   0001_9_high.png
            │   0002_high.png
            │   0002_0_high.png
            │   0002_1_high.png
            │   ...
        └───Flood
            │   0001_high.png
            │   0001_0_high.png
            │   0001_1_high.png
            │   ...
            │   0001_9_high.png
            │   0002_high.png
            │   0002_0_high.png
            │   0002_1_high.png
            │   ...
        └───JSON
            │   0001_high.json
            │   0001_0_high_high.json
            │   0001_1_high_high.json
            │   ...
            │   0001_9_high_high.json
            │   0002_high.json
            │   0002_0_high_high.json
            │   0002_1_high_high.json
            │   ...
        └───Mask
            │   0001_high.png
            │   0001_0_high.png
            │   0001_1_high.png
            │   ...
            │   0001_9_high.png
            │   0002_high.png
            │   0002_0_high.png
            │   0002_1_high.png
            │   ...
        └───Normal
            │   0001_high.png
            │   0001_0_high.png
            │   0001_1_high.png
            │   ...
            │   0001_9_high.png
            │   0002_high.png
            │   0002_0_high.png
            │   0002_1_high.png
            │   ...
        └───Segmentation
            │   0001_high.png
            │   0001w_high.png
            │   0001_0_high.png
            |   0001_0w_high_high.png
            │   0001_1_high.png
            |   0001_1w_high_high.png
            │   ...
```

```
Mila-Simulated-flood-19800-low
└───Mila-Simulated-flood
    └───Unity-19800-low
        └───Depth
            │   0001_low.png
            │   0001_0_low.png
            │   0001_1_low.png
            │   ...
            │   0001_9_low.png
            │   0002_low.png
            │   0002_0_low.png
            │   0002_1_low.png
            │   ...
        └───Flood
            │   0001_low.png
            │   0001_0_low.png
            │   0001_1_low.png
            │   ...
            │   0001_9_low.png
            │   0002_low.png
            │   0002_0_low.png
            │   0002_1_low.png
            │   ...
        └───JSON
            │   0001_low.json
            │   0001_0_low.json
            │   0001_1_low.json
            │   ...
            │   0001_9_low.json
            │   0002_low.json
            │   0002_0_low.json
            │   0002_1_low.json
            │   ...
        └───Mask
            │   0001_low.png
            │   0001_0_low.png
            │   0001_1_low.png
            │   ...
            │   0001_9_low.png
            │   0002_low.png
            │   0002_0_low.png
            │   0002_1_low.png
            │   ...
        └───Normal
            │   0001_low.png
            │   0001_0_low.png
            │   0001_1_low.png
            │   ...
            │   0001_9_low.png
            │   0002_low.png
            │   0002_0_low.png
            │   0002_1_low.png
            │   ...
        └───Segmentation
            │   0001_low.png
            │   0001w_low.png
            │   0001_0_low.png
            |   0001_0w_low.png
            │   0001_1_low.png
            |   0001_1w_low.png
            │   ...
```
## Details of the Dataset
The data from the simulator provides for each snapshot of the world: 
- Original image (non-flooded)
- Flooded image 
- Binary mask of the area of the flood
- Depth image
- Semantic segmentation image : for both flooded and non-flooded scenario.
- json file with camera parameters

### Depth images
The depth maps are provided as RGBA images. Depth is encoded in the the following way: 
 - The information from the simulator is (1 - LinearDepth (in [0,1])).   
 `far` corresponds to the furthest distance to the camera included in the depth map. 
        `LinearDepth * far` gives the real metric distance to the camera. 
- depth is first divided in 31 slices encoded in the R channel with values ranging from 0 to 247 
- each slice is divided again in 31 slices, whose values are encoded in the G channel
- each of the G slices is divided into 256 slices, encoded in the B channel
    In total, we have a discretization of depth into `N = 31*31*256 - 1` possible values, each value covering a range of 
    far/N meters.   
    Note that, what we encode here is  `1 - LinearDepth` so that the furthest point is [0,0,0] (which is sky) 
    and the closest point is [255,255,255] 
    The metric distance associated to a pixel whose depth is (R,G,B) is : 
    d = (far/N) * [((247 - R)//8)*256*31 + ((247 - G)//8)*256 + (255 - B)]  
    This is the same as :
    d = far* ( 1 - ((R//8)*256*31 + (G//8)*256 + B)/N )
    
### Segmentation images 
Segmentation masks are provided for the flooded version of the images. The 10 classes were merged from the [Cityscapes](https://www.cityscapes-dataset.com/) dataset labels. 
The following table provides the correspondence between classes and colors: 

 
| Label         | Description                                                     | RGBA               | Cityscapes labels     |
| ------------- | --------------------------------------------------------------- | ------------------ | --------------------- |
| Water         | Water generated by the simulator                                | [0, 0, 255, 255]   | None                  |
| Ground        | Horizontal ground-level structures (road, roundabouts, parking) | [55, 55, 55, 255]  | 0, 1 (Road, Sidewalk) |
| Building      | Buildings, walls, fences                                        | [0, 255, 255, 255] | 2, 3, 4               |
| Traffic items | Poles, traffic signs, traffic lights                            | [255, 212, 0, 255] | 5, 6, 7               |
| Vegetation    | Trees, hedges, all kinds of vertical vegetation                 | [0, 255, 0, 255]   | 8                     |
| Terrain       | Grass, all kinds of horizontal vegetation, soil, sand           | [255, 97, 0, 255]  | 9                     |
| Sky           | Open sky                                                        | [0, 0, 0, 255]     | 10                    |
| Car           | This includes only cars                                         | [255, 0, 0, 255]   | 13                    |
| Trees         | Some trees are seen as 2D in Unity and not segmented            | [0, 0, 0, 0]       |
| Truck         | Vehicle with greater dimensions  than car                       |                    | 14, 15, 16            |
| Person        | Not in the dataset                                              |                    | 11, 12                |

 <!--- Note: figure out the Tree labels, since this may introduce noise in the training --->
Even though some categories are not yet included in the simulated dataset, we choose specific colors to represent them in order to convert segmentation maps obtained with 19-class cityscapes to our simulated dataset labels. 

### JSON files

The json files contain the following information:
- `CameraPosition`: camera *absolute* coordinates  in meters- the origin is not the ground but the origin of the simulated world
- `CameraRotation`: pitch (x) , yaw (y), roll (z) in degrees from 0 to 360 (for pitch the direction of the rotation is from down to up)
- `CameraFar`: how far we compute the depth map 
- `CameraFOV`: vertical field of view in degrees
- `WaterLevel`: absolute level of water in meters


## References
If you use MILA Simulated Floods Dataset please cite the related paper:
```
@article{xxx,
  title={xxx},
  author={xxx},
  journal={arxiv},
  year={2021}
}
```

## Credits
**Placeholder**
