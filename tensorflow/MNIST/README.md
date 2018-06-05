## [MNIST](http://yann.lecun.com/exdb/mnist/)  
MNIST is a subset of a larger set available from NIST. The digits have been size-normalized and centered in a fixed-size image.  
It is a good database for people who want to try learning techniques and pattern recognition methods on real-world data while spending minimal efforts on preprocessing and formatting.  
The original black and white (bilevel) images from NIST were size normalized to fit in a 20x20 pixel box while preserving their aspect ratio. The resulting images contain grey levels as a result of the anti-aliasing technique used by the normalization algorithm. the images were centered in a 28x28 image by computing the center of mass of the pixels, and translating the image so as to position this point at the center of the 28x28 field.  
With some classification methods (particuarly template-based methods, such as SVM and K-nearest neighbors), the error rate improves when the digits are centered by bounding box rather than center of mass. If you do this kind of pre-processing, you should report it in your publications.
### FILE FORMATS FOR THE MNIST DATABASE
The data is stored in a very simple file format designed for storing vectors and multidimensional matrices.  
All the integers in the files are stored in the MSB first (high endian) format used by most non-Intel processors. Users of Intel processors and other low-endian machines must flip the bytes of the header.  
There are 4 files:  
train-images.idx3-ubyte: training set images  
train-labels.idx1-ubyte: training set labels  
t10k-images.idx3-ubyte:  test set images  
t10k-labels.idx1-ubyte:  test set labels  
The training set contains 60000 examples, and the test set 10000 examples.
#### TRAINING SET LABEL FILE (train-labels-idx1-ubyte)
|offset|type|value|description|
|-|-|-|-|
|0000|32 bit integer|0x00000801(2049) magic number|(MSB first)|
|0004|32 bit integer|60000|number of items|
|0008|unsigned byte|??|label|
|0009|unsgined byte|??|label|
|xxxx|unsgined byte|??|label|

The labels values are 0 to 9.
#### TRAINING SET IMAGE FILE (train-images-idx3-ubyte)
|offset|type|value|description|
|-|-|-|-|
|0000|32 bit interger|0x00000803(2051) magic number||
|0004|32 bit interger|60000|number of images|
|0008|32 bit interger|28|number of rows|
|0012|32 bit interger|28|number of columns|
|0016|unsigned byte|??|pixel|
|0017|unisgned byte|??|pixel|
|xxxx|unsigned byte|??|pixel|

Pixels are organized row-wise. Pixel values are 0 to 255. 0 means background (white), 255 means foreground (black).
#### TEST SET LABEL FILE (t10k-labels-idx1-ubyte)
|offset|type|value|description|
|-|-|-|-|
|0000|32 bit integer|0x00000801(2049) magic number|(MSB first)|
|0004|32 bit integer|10000|number of items|
|0008|unsigned byte|??|label|
|0009|unsgined byte|??|label|
|xxxx|unsgined byte|??|label|

The labels values are 0 to 9.
#### TEST SET IMAGE FILE (t10k-images-idx3-ubyte)
|offset|type|value|description|
|-|-|-|-|
|0000|32 bit interger|0x00000803(2051) magic number||
|0004|32 bit interger|10000|number of images|
|0008|32 bit interger|28|number of rows|
|0012|32 bit interger|28|number of columns|
|0016|unsigned byte|??|pixel|
|0017|unisgned byte|??|pixel|
|xxxx|unsigned byte|??|pixel|

Pixels are organized row-wise. Pixel values are 0 to 255. 0 means background (white), 255 means foreground (black).