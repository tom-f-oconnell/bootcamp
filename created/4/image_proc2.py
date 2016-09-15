
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import skimage.io
import skimage.measure
import skimage.filters
import skimage.segmentation

sns.set_style('dark')

# load an example phase image
phase_im = skimage.io.imread('../../data/HG105_images/noLac_phase_0004.tif')

# show the image
plt.imshow(phase_im, cmap=plt.cm.viridis)
plt.show()
