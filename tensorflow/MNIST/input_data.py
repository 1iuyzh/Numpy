import struct
import numpy as np
import matplotlib.pyplot as plt

train_images_idx3_ubyte = './dataset/MNIST/train-images.idx3-ubyte'
train_labels_idx1_ubyte = './dataset/MNIST/train-labels.idx1-ubyte'
test_images_idx3_ubyte = './dataset/MNIST/t10k-images.idx3-ubyte'
test_lables_idx1_ubyte = './dataset/MNIST/t10k-labels.idx1-ubyte'

# 解析idx文件
def decode_idx_ubyte(path):
    # 读取二进制数据
    buffer = open(path, 'rb').read()
    # 解析头信息
    offset = 0
    head_format = '>i' # big-endian
    magic_number = struct.unpack_from(head_format, buffer, offset)[0]
    if magic_number == 2049: # idx1
        # print('magic number: %d' % magic_number)
        offset += struct.calcsize(head_format)
        head_format = '>i'
        num_items = struct.unpack_from(head_format, buffer, offset)[0]
        # print('number of items: %d' % num_items)
        # 解析数据集
        offset += struct.calcsize(head_format)
        label_format = '>B'
        labels = np.empty(num_items)
        for i in range(num_items):
            labels[i] = struct.unpack_from(label_format, buffer, offset)[0]
            offset += struct.calcsize(label_format)
        return labels # (60000, 1)
    if magic_number == 2051: # idx3
        # print('magic number: %d' % magic_number)
        offset += struct.calcsize(head_format)
        head_format = '>iii'
        num_images, num_rows, num_cols = struct.unpack_from(head_format, buffer, offset)
        # print('number of images: %d, number of rows: %d, number of columns: %d' % (num_images, num_rows, num_cols))
        # 解析数据集
        image_size = num_rows * num_cols
        offset += struct.calcsize(head_format)
        image_format = '>' + str(image_size) + 'B'
        images = np.empty([num_images, num_rows, num_cols])
        for i in range(num_images):
            images[i] = np.array(struct.unpack_from(image_format, buffer, offset)).reshape([num_rows, num_cols])
            offset += struct.calcsize(image_format)
        return images # (60000, 28, 28)

# 测试
def test():
    train_images = decode_idx_ubyte(train_images_idx3_ubyte)
    train_labels = decode_idx_ubyte(train_labels_idx1_ubyte)
    print(train_images.shape)
    print(train_labels.shape)
    for i in range(10):
        print(train_labels[i])
        plt.imshow(train_images[i], cmap = 'gray')
        plt.show()

if __name__ == '__main__':
    test()