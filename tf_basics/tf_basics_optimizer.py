import tensorflow as tf

W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

linear_model = W * x + b
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)

init = tf.global_variables_initializer()
sess = tf.Session()

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)
sess.run(init)

for i in range(1000):
  sess.run(train, { x: [1, 2, 3, 4], y: [0, -1, -2, -3] })

print(sess.run([W, b]))


