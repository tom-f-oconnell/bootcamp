
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
plt.title('Original phase image')

# substracting out a blurred version of the image to approximate background subtraction
# second argument is a pixel dimension of filter, i think
im_blur = skimage.filters.gaussian(phase_im, 50.0)

#plt.imshow(im_blur, cmap=plt.cm.viridis)
#plt.show()

# need to convert data types to background subtract
phase_float = skimage.img_as_float(phase_im)
phase_sub = phase_float - im_blur

#plt.figure()
#plt.title('Guassian blur subtracted, filter size = 50px')
#plt.imshow(phase_sub, cmap=plt.cm.viridis)

# otsu's method on background subtracted image
phase_sub_thresh = skimage.filters.threshold_otsu(phase_sub)
# segmentation based on threshold
phase_seg = phase_sub < phase_sub_thresh

#plt.imshow(phase_seg, cmap=plt.cm.Greys_r)

seg_lab, num_cells = skimage.measure.label(phase_seg, return_num=True, background=0)
#plt.close('all')
# this colormap looks kinda like the 'jet' they were railing against
#plt.imshow(seg_lab, cmap=plt.cm.Spectral_r)

# compute the regionprops and extract area of each object
ip_dist = 0.063 # um per pixel (center-center, i assume)

# why isn't 0 background? is the background label included here? TODO
props = skimage.measure.regionprops(seg_lab)

areas = np.array([prop.area for prop in props])
cutoff = 300

# make a copy since we will be changing this image in the loop below
im_cells = np.copy(seg_lab) > 0

for i in range(len(areas)):
    if areas[i] < cutoff:
        im_cells[seg_lab == props[i].label] = 0

# what does this do?
area_filt_lab = skimage.measure.label(im_cells)
plt.figure()
plt.imshow(area_filt_lab, cmap=plt.cm.Spectral_r)

plt.show()
