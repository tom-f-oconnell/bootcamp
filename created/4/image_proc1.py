
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# for image processing
import skimage.io
# for histograms
import skimage.exposure
# for median filtering
import skimage.morphology

# what does this really do?
sns.set()

# load the images
phase_im = skimage.io.imread('../../data/bsub_100x_phase.tif')
cfp_im = skimage.io.imread('../../data/bsub_100x_cfp.tif')

# show the phase image
# plt.imshow(phase_im, cmap=plt.cm.Greys_r)
#plt.imshow(phase_im, cmap=plt.cm.viridis)
#plt.show()

# plot the histogram of phase image
#hist_phase, bins_phase = skimage.exposure.histogram(phase_im)
#plt.plot(bins_phase, hist_phase)
#plt.xlabel('pixel value')
#plt.ylabel('count')
#plt.show()

# apply a threshold to our image
thresh = 220
im_phase_thresh = phase_im < thresh

#with sns.axes_style('dark'):
#    plt.imshow(im_phase_thresh, cmap=plt.cm.Greys_r)
#    plt.show()

with sns.axes_style('dark'):
    plt.imshow(cfp_im, cmap=plt.cm.viridis)
    plt.show()

# slice out region with hot pixel (most intense and causing poor scaling of other values)
#selem = skimage.morphology.disk(1)
#plt.imshow(selem)
#plt.imshow(selem, interpolation='nearest')

# here it is
# np.sum(cfp_im > 225)

selem = skimage.morphology.square(3)
cfp_filt = skimage.filters.median(cfp_im, selem)

# alternative to this context managing syntax? this seems to be the norm not the exception
with sns.axes_style('dark'):
    plt.imshow(cfp_filt, cmap=plt.cm.viridis)
    plt.show()

# if the hot pixels are really consistent, are there some other built tools to use that info?
# seems median filter would lose (some) edge information for segmentation


