from scipy.misc import imread, imsave, imresize
# Read a JPEG image into a numpy array
img = imread('assets/cat.jpg')
print(img.dtype, img.shape)
img_tinted = img * [1, 0.95, 0.9]
img_tinted = imresize(img_tinted, (300, 300))
imsave('assets/cat_tinted.jpg', img_tinted)