import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import input

train_images_idx3_ubyte = './tensorflow/MNIST/data/train-images.idx3-ubyte'
train_labels_idx1_ubyte = './tensorflow/MNIST/data/train-labels.idx1-ubyte'
test_images_idx3_ubyte = './tensorflow/MNIST/data/t10k-images.idx3-ubyte'
test_lables_idx1_ubyte = './tensorflow/MNIST/data/t10k-labels.idx1-ubyte'

train_images = input.decode_idx_ubyte(train_images_idx3_ubyte)
train_labels = input.decode_idx_ubyte(train_labels_idx1_ubyte)
test_images = input.decode_idx_ubyte(test_images_idx3_ubyte)
test_lables = input.decode_idx_ubyte(test_lables_idx1_ubyte)

if __name__ == '__main__':
    for i in range(10):
        print(train_labels[i])
        plt.imshow(train_images[i], cmap = 'gray')
        plt.show()