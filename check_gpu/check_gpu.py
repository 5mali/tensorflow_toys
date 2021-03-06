import tensorflow as tf

sess_dummy = tf.Session(config=tf.ConfigProto(log_device_placement=True))


with tf.device('/cpu:0'):
    a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
    b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
    c = tf.matmul(a, b)

with tf.Session() as sess_cpu:
    print(sess_cpu.run(c))

# with tf.device('/gpu:0'):
    # a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
    # b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
    # c = tf.matmul(a, b)

# with tf.Session() as sess_gpu:
    # print(sess_gpu.run(c))
