
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

import scipy.optimize as sopt

def gradient_model(x, I_0, lam):
    """Model for colony fluorescence gradient: exponential growth plus a constant background. """

    assert np.any(np.array(x) >= 0)
    assert np.any(np.array([I_0, lam]) >= 0)

    return I_0 * np.exp(x / lam)

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

xmax, ymax = stack[0].shape
bar_height = 3 # pixels
scale_length = 10 # um
interpixel_dist = 0.0636 # um (reported in exercise) consistent across datasets?
scale_pixel_length = round(scale_length / interpixel_dist)

# burn a scale bar in to the data
# do not save this manipulated data over original, of course
for i in range(len(stack)):
    end = round(xmax * 0.9)
    ycoord = round(ymax * 0.9)
    # max 16bit value
    stack[i][end - scale_pixel_length : end, ycoord : ycoord + bar_height] = 65535

# Build RGB image by stacking grayscale images
im_rgb = np.dstack(3 * [stack[i] / stack[i].max()])
labeled = seg_stack[i] > 0

# Only show green channel on bacteria
im_rgb[labeled, 0] = 0
im_rgb[labeled, 1] = seg_stack[i][labeled]
im_rgb[labeled, 2] = 0

#plt.imshow(im_rgb)
#plt.title('Segmented version of the ' + str(i) + 'th image')
#plt.show()

sums = np.zeros(len(stack))

# sum the fluorescence within all segmented regions per stack to monitor growth
for i in range(len(stack)):
    sums[i] = stack[i][seg_stack[i] > 0].sum()

# perform an exponential regression to fit the curve
I_0_guess = 1
lam_guess = 0.5
s0 = np.array([I_0_guess, lam_guess])

ts = np.arange(0, len(sums))
s_opt, _ = sopt.curve_fit(gradient_model, ts, sums, p0=s0)

x_smooth = np.linspace(0, 1, 200)
I_smooth = gradient_model(x_smooth, *tuple(s_opt))

plt.close('all')

plt.plot(ts, sums, marker='.', linestyle='none', color='r')
plt.plot(x_smooth, I_smooth, color='gray')

plt.xlabel('Time point')
plt.ylabel('Total fluorescence in segmented region')
plt.title('Colony growth through area')

plt.show()
