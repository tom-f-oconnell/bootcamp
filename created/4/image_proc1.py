
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# for image processing
import skimage.io
# for histograms
import skimage.exposure

# what does this really do?
sns.set()

# load the images
phase_im = skimage.io.imread('../../data/bsub_100x_phase.tif')
cfp_im = skimage.io.imread('../../data/bsub_100x_cfp.tif')

# show the phase image
# plt.imshow(phase_im, cmap=plt.cm.Greys_r)
plt.imshow(phase_im, cmap=plt.cm.viridis)
plt.show()

# plot the histogram of phase image
hist_phase, bins_phase = skimage.exposure.histogram(phase_im)
