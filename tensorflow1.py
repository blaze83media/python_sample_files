import tensorflow as tf           #tensorflow version 1
a=tf.Variable(0.)
b=tf.Variable(1.)

op_add=a.assign(a+b)
op_mul=b.assign(b*2)
init=tf.global_variables_initializer

with tf.Session() as sess:
    init.run()
    for iteration in range(50):
        sess.run(add_op)
        sess.run(mul_op)
    print(a.eval())
    
    
    
    
 #import tensorflow as tf           #tensorflow version 2 
tf.enable_eager_execution()

a=tf.contrib.eager.Variable(0.)
b=tf.contrib.eager.Variable(1.)

for iteration in range(50):
    a.assign(a+b)
    b.assign(b*2)
    print(a.numpy())
    
    
##########################################################################
    
    # Construct the Graph
  g = tf.Graph()
  with g.as_default():
 
      if init_weights:
          self._n_classes = np.max(y) + 1
          self._n_features = X.shape[1]
          tf_weights_, tf_biases_ = self._initialize_weights(
              n_features=self._n_features,
              n_classes=self._n_classes)
          self.cost_ = []
      else:
          tf_weights_ = tf.Variable(self.weights_)
          tf_biases_ = tf.Variable(self.biases_)
 
      # Prepare the training data
      y_enc = self._one_hot(y, self._n_classes)
      n_idx = list(range(y.shape[0]))
      tf_X = tf.convert_to_tensor(value=X, dtype=self.dtype)
      tf_y = tf.convert_to_tensor(value=y_enc, dtype=self.dtype)
      tf_idx = tf.placeholder(tf.int32,
                              shape=[int(y.shape[0] / n_batches)])
      X_batch = tf.gather(params=tf_X, indices=tf_idx)
      y_batch = tf.gather(params=tf_y, indices=tf_idx)
 
      # Setup the graph for minimizing cross entropy cost
      logits = tf.matmul(X_batch, tf_weights_) + tf_biases_
      cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits,
                                                              y_batch)
      cost = tf.reduce_mean(cross_entropy)
      optimizer = tf.train.GradientDescentOptimizer(
          learning_rate=self.eta)
      train = optimizer.minimize(cost)
 
      # Initializing the variables
      init = tf.initialize_all_variables()