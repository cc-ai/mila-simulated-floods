# MILA Simulated Floods Dataset

## Dataset presentation
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
