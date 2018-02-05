import tensorflow as tf

sess = tf.Session()
node1 = tf.constant(3)
node2 = tf.constant(4)
node3 = tf.add(node1, node2)
print(sess.run(node3))