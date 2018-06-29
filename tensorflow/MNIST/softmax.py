import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import input_data
import random

train_images, train_labels, test_images, test_labels = input_data.get_data()

# model
x = tf.placeholder('float', [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b) # tf.matmul

# strategy
y_ = tf.placeholder('float', [None, 10])
cross_entropy = -tf.reduce_sum(y_ * tf.log(y)) # tf.reduce_sum

# algorithm
train = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

# initialization
init = tf.global_variables_initializer()

# run
sess = tf.Session()
sess.run(init)

# train
for i in range(1000):
    index = random.sample(range(train_images.shape[0]), 100)
    batch_xs = train_images[index]
    batch_ys = train_labels[index]
    sess.run(train, feed_dict = {x: batch_xs, y_: batch_ys})

# evaluation
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1)) # tf.equal
accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float')) # tf.cast
print(sess.run(accuracy, feed_dict = {x: test_images[0:10], y_: test_labels[0:10]}))

# verification
result = tf.argmax(y, 1) # tf.argmax
for i in range(3):
    index = random.randint(0, test_images.shape[0] - 1)
    label = sess.run(result, feed_dict = {x: test_images[index:index + 1], y_: test_labels[index:index + 1]}) # 不降维
    print(label[0])
    image = test_images[index].reshape(28, 28) * 255
    plt.imshow(image, cmap = 'gray')
    plt.show()