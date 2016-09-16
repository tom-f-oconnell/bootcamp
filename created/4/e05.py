
import numpy as np
import skimage.io
import skimage.measure
import skimage.filters
import skimage.segmentation
# for listing all image files in the directory
import os
import matplotlib.pyplot as plt
import seaborn as sns
import image_proc_practice as improc

sns.set_style('dark')

image_path = '../../data/bacterial_growth/'
bac_tifs = [image_path + f for f in os.listdir(image_path) if os.path.isfile(image_path + f)]
bac_tifs = sorted(bac_tifs)
# remove the first element after sorting, because that should be the README
bac_tifs = bac_tifs[1:]

# could also be a numpy tensor, but this could avoid some slicing clunkiness
stack = [None] * len(bac_tifs)

for i, f in enumerate(bac_tifs):
    stack[i] = skimage.io.imread(f)

i = np.random.randint(0, len(stack))
plt.imshow(stack[i], cmap=plt.cm.viridis)
plt.title('Original image from the ' + str(i) + 'th image')

plt.show()
