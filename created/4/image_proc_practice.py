
import numpy as np
import skimage.io
import skimage.measure
import skimage.filters
import skimage.segmentation

def segment(img, thresh=None, med_width=3, blur_width=50, area_thresh=300):
    """ Returns a labeled segmentation mask """
    
    # median filter to deal with 'hot'/bad pixels
    selem = skimage.morphology.square(med_width)
    img_filt = skimage.filters.median(img, selem)
    
    # substracting out a blurred version of the image to approximate background subtraction
    # second argument is a pixel dimension of filter, i think
    img_blur = skimage.filters.gaussian(img_filt, filt_width)
    
    # need to convert data types to background subtract
    img_float = skimage.img_as_float(img)
    assert img_float.dtype == img_blur.dtype
    img_sub = img_float - img_blur
    
    if thresh == None:
        thresh = skimage.filters.threshold_otsu(img_sub)

    img_thresh = img_sub > thresh
     
    seg_lab, num_cells = skimage.measure.label(phase_seg, return_num=True, background=0)
    # why isn't 0 background? is the background label included here? TODO
    props = skimage.measure.regionprops(seg_lab)
    areas = np.array([prop.area for prop in props])
    
    # make a copy since we will be changing this image in the loop below
    im_cells = np.copy(seg_lab) > 0
    
    for i in range(len(areas)):
        if areas[i] < area_thresh:
            im_cells[seg_lab == props[i].label] = 0
        
        print(props[i].coords)
    
    # what does this do?
    area_filt_lab = skimage.measure.label(im_cells)
    
    # remove objects near / touching image border TODO
    # pos_filt_lab = sk

    return area_filt_lab

# cfp_im = skimage.io.imread('../../data/bsub_100x_cfp.tif')
