
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

import time

sns.set_style('dark')

image_path = '../../data/bacterial_growth/'
bac_tifs = [image_path + f for f in os.listdir(image_path) if os.path.isfile(image_path + f)]
bac_tifs = sorted(bac_tifs)
# remove the first element after sorting, because that should be the README
bac_tifs = bac_tifs[1:]

# could also be a numpy tensor, but this could avoid some slicing clunkiness
stack = [None] * len(bac_tifs)

plt.figure()

for i, f in enumerate(bac_tifs):
    stack[i] = skimage.io.imread(f)
    # won't display until terminated / interrupted
    #plt.imshow(stack[i], cmap=plt.cm.viridis)
    #plt.show()
    #print('allp')
    #time.sleep(0.5)

i = np.random.randint(0, len(stack))
plt.imshow(stack[i], cmap=plt.cm.viridis)
plt.title('Original image from the ' + str(i) + 'th image')
plt.show()

seg_stack = [None] * len(bac_tifs)

for i, img in enumerate(stack):
    print('Segmenting ' + str(i) + 'th image.')
    seg_stack[i] = improc.segment(img)

plt.figure()
i = np.random.randint(0, len(stack))

# Build RGB image by stacking grayscale images
im_rgb = np.dstack(3 * [stack[i] / stack[i].max()])
labeled = seg_stack[i] > 0

# Only show green channel on bacteria
im_rgb[labeled, 0] = 0
im_rgb[labeled, 1] = seg_stack[i][labeled]
im_rgb[labeled, 2] = 0

plt.imshow(im_rgb)

plt.title('Segmented version of the ' + str(i) + 'th image')
plt.show()

