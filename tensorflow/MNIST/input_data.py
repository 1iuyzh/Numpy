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
    head_format = '>i' # big-endian 字节序
    magic_number = struct.unpack_from(head_format, buffer, offset)[0]
    offset += struct.calcsize(head_format)
    if magic_number == 2049: # labels
        head_format = '>i'
        num_items = struct.unpack_from(head_format, buffer, offset)[0]
        # 解析数据集
        offset += 4
        label_format = '>B'
        labels = np.empty(num_items)
        for i in range(num_items):
            labels[i] = struct.unpack_from(label_format, buffer, offset)[0]
            offset += 1
        return labels
    if magic_number == 2051: # images
        head_format = '>3i'
        num_images, num_rows, num_cols = struct.unpack_from(head_format, buffer, offset)
        # 解析数据集
        offset += struct.calcsize(head_format)
        image_size = num_rows * num_cols
        image_format = '>' + str(image_size) + 'B'
        images = np.empty([num_images, num_rows, num_cols])
        for i in range(num_images):
            images[i] = np.array(struct.unpack_from(image_format, buffer, offset)).reshape([num_rows, num_cols])
            offset += struct.calcsize(image_format)
        return images

def get_data():
    images = decode_idx_ubyte(train_images_idx3_ubyte)
    train_images = images.reshape([images.shape[0], -1]) / 255 # (60000, 784)

    labels = decode_idx_ubyte(train_labels_idx1_ubyte)
    train_labels = np.zeros([labels.shape[0], 10])
    for i in range(labels.shape[0]):
        train_labels[i][int(labels[i])] = 1 # (60000, 10)
    
    images = decode_idx_ubyte(test_images_idx3_ubyte)
    test_images = images.reshape([images.shape[0], -1]) / 255 # (10000, 784)

    labels = decode_idx_ubyte(test_lables_idx1_ubyte)
    test_labels = np.zeros([labels.shape[0], 10])
    for i in range(labels.shape[0]):
        test_labels[i][int(labels[i])] = 1 # (10000, 10)
    
    return train_images, train_labels, test_images, test_labels

# 测试
def test():
    train_images = decode_idx_ubyte(train_images_idx3_ubyte)
    train_labels = decode_idx_ubyte(train_labels_idx1_ubyte)
    for i in range(3):
        print(train_labels[i])
        plt.imshow(train_images[i], cmap = 'gray')
        plt.show()

if __name__ == '__main__':
    test()