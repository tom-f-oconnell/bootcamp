
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
    img_blur = skimage.filters.gaussian(img_filt, blur_width)
    
    # need to convert data types to background subtract
    img_float = skimage.img_as_float(img)
    assert img_float.dtype == img_blur.dtype
    img_sub = img_float - img_blur
    
    if thresh == None:
        thresh = skimage.filters.threshold_otsu(img_sub)

    # TODO maybe reverse inequality
    img_thresh = img_sub > thresh
     
    seg_lab, num_cells = skimage.measure.label(img_thresh, return_num=True, background=0)
    # why isn't 0 background? is the background label included here? TODO
    props = skimage.measure.regionprops(seg_lab)
    areas = np.array([prop.area for prop in props])
    
    # make a copy since we will be changing this image in the loop below
    im_cells = np.copy(seg_lab) > 0

    # get a representation of the borders, so we can check if blocks intersect them
    x_size, y_size = img.shape
    x_range1 = np.zeros((x_size, 2), dtype=int)
    y_range1 = np.zeros((y_size, 2), dtype=int)
    x_range2 = np.zeros((x_size, 2), dtype=int)
    y_range2 = np.zeros((y_size, 2), dtype=int)

    # set one of each of the ranges to the extreme values of the other dimension (0 and max)
    x_range1[:,0] = np.arange(0, x_size, dtype=int)
    x_range1[:,1] = np.ones(x_size, dtype=int) * y_size
    x_range2[:,0] = np.arange(0, x_size, dtype=int)

    y_range1[:,1] = np.arange(0, y_size, dtype=int)
    y_range1[:,0] = np.ones(y_size, dtype=int) * x_size
    y_range2[:,1] = np.arange(0, y_size, dtype=int)

    # TODO test more, but seems right
    # print(x_range1)
    # print(y_range2)
    
    for i in range(len(areas)):
        # filter out things too small
        if areas[i] < area_thresh:
            im_cells[seg_lab == props[i].label] = 0
        
        # an example of a way to see if a coord is in a set
        #print(np.array([834, 115]) in props[i].coords)

        # filter out blobs ACTUALLY INCLUDING one of the edge coordinates
        for c in props[i].coords:
            if c in x_range1 or c in x_range2 or c in y_range1 or c in y_range2:
                im_cells[seg_lab == props[i].label] = 0
    
    # what does this do?
    area_filt_lab = skimage.measure.label(im_cells)
    
    # remove objects near / touching image border TODO
    # pos_filt_lab = sk

    return area_filt_lab

# cfp_im = skimage.io.imread('../../data/bsub_100x_cfp.tif')
