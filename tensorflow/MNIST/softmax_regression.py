import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import input_data
import random

train_images_idx3_ubyte = './dataset/MNIST/train-images.idx3-ubyte'
train_labels_idx1_ubyte = './dataset/MNIST/train-labels.idx1-ubyte'
test_images_idx3_ubyte = './dataset/MNIST/t10k-images.idx3-ubyte'
test_lables_idx1_ubyte = './dataset/MNIST/t10k-labels.idx1-ubyte'

# 输入
train_images = input_data.decode_idx_ubyte(train_images_idx3_ubyte)
train_images = train_images.reshape([train_images.shape[0], -1]) / 255 # (60000, 784) 像素值[0, 1]

labels = input_data.decode_idx_ubyte(train_labels_idx1_ubyte)
train_labels = np.zeros([labels.shape[0], 10])
for i in range(labels.shape[0]):
    train_labels[i][int(labels[i])] = 1 # one-hot (60000, 10)

test_images = input_data.decode_idx_ubyte(test_images_idx3_ubyte)
test_images = test_images.reshape([test_images.shape[0], -1]) / 255 # (10000, 784) nan

labels = input_data.decode_idx_ubyte(test_lables_idx1_ubyte)
test_labels = np.zeros([labels.shape[0], 10])
for i in range(labels.shape[0]):
    test_labels[i][int(labels[i])] = 1 # (10000, 10)

# 模型
x = tf.placeholder('float', [None, 784]) # tensor
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b) # softmax回归

# 策略
y_ = tf.placeholder('float', [None, 10])
cross_entropy = -tf.reduce_sum(y_ * tf.log(y)) # 交叉熵 tf.log

# 算法
train = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy) # 梯度下降

# 初始化变量
init = tf.global_variables_initializer()

# 启动图
sess = tf.Session()
sess.run(init)

# 训练
for i in range(1000):
    index = random.sample(range(train_images.shape[0]), 100) # 随机训练
    batch_xs = train_images[index]
    batch_ys = train_labels[index]
    sess.run(train, feed_dict = {x: batch_xs, y_: batch_ys})

# 评估
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1)) # tf.equal
accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float')) # tf.cast
print(sess.run(accuracy, feed_dict = {x: test_images[0:10], y_: test_labels[0:10]}))

# 验证
result = tf.argmax(y, 1) # 预测结果 tf.argmax
for i in range(10):
    index = random.randint(0, test_images.shape[0] - 1)
    label = sess.run(result, feed_dict = {x: test_images[index:index + 1], y_: test_labels[index:index + 1]}) # index不降维
    print(label[0])
    image = test_images[index].reshape(28, 28) * 255
    plt.imshow(image, cmap = 'gray')
    plt.show()