import tensorflow as tf
import numpy as np

x_data = np.float32(np.random.rand(2, 100))
y_data = np.dot([0.1, 0.2], x_data) + 0.3

# 模型
b = tf.Variable(tf.zeros([1])) # tf.Variable 变量
W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0)) # tf.random_uniform 均匀分布随机数
y = tf.matmul(W, x_data) + b # tf.matmul 矩阵乘法

# 策略
loss = tf.reduce_mean(tf.square(y - y_data)) # tf.reduce_mean 求平均值
optimizer = tf.train.GradientDescentOptimizer(0.5) # 梯度下降
train = optimizer.minimize(loss)

# 初始化变量
init = tf.initialize_all_variables()

# 启动图
sess = tf.Session()
sess.run(init)

# 拟合平面
for step in range(0, 201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))