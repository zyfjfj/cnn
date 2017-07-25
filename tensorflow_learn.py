import tensorflow as tf

node1=tf.constant(3.0,dtype=tf.float32)
node2=tf.constant(4.0)
node3=tf.add(node1,node2)
a=tf.placeholder(tf.float32)
b=tf.placeholder(tf.float32)
add_node=a*b
W=tf.Variable([.3],dtype=tf.float32)
b=tf.Variable([-.3],dtype=tf.float32)
x=tf.placeholder(tf.float32)
linear_model=W*x+b
y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    # print(sess.run([node3]))
    # print(sess.run(add_node,{a:[1,3],b:[3,4.5]}))
    print(sess.run(linear_model,{x:6}))
    # fixW = tf.assign(W, [-1.])
    # fixb = tf.assign(b, [10.])
    # sess.run([fixW, fixb])
    # print(sess.run(linear_model,{x:6}))
    print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))

import numpy as np

x_data=np.float32(np.random.rand(2,100))
y_data=np.dot([0.1,0.2],x_data)+0.3
print(y_data.shape)