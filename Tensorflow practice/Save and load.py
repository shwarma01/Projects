import os
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout, Dense
from tensorflow.keras import regularizers

print(f"-------------------{tf.__version__}---------------------")

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

y_train = y_train[:1000]
y_test = y_test[:1000]

X_train = X_train[:1000].reshape(-1, 28 * 28) / 255.0
X_test = X_test[:1000].reshape(-1, 28 * 28) / 255.0

# Define a simple sequential model
def create_model():
  model = Sequential([
    Dense(512, activation='relu', input_shape=(784,), kernel_regularizer = regularizers.l2(0.001)),
    Dropout(0.2),
    Dense(10)
  ])

  model.compile(optimizer = 'adam',
                loss = tf.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics = ['accuracy'])

  return model

# Create a basic model instance
model = create_model()

# Display the model's architecture
model.summary()

checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Create a callback that saves the model's weights
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath = checkpoint_path,
                                                 save_weights_only = True,
                                                 verbose = 1)

# Train the model with the new callback
model.fit(X_train,
          y_train,
          epochs = 10,
          validation_data = (X_test, y_test),
          callbacks = [cp_callback])  # Pass callback to training

# Create a basic model instance
model = create_model()

# Evaluate the model
loss, acc = model.evaluate(X_test,  y_test, verbose = 2)
print(f"Untrained model, accuracy: {100 * acc : 5.2f}")

# Loads the weights
model.load_weights(checkpoint_path)

# Re-evaluate the model
loss,acc = model.evaluate(X_test,  y_test, verbose = 2)
print(f"Untrained model, accuracy: {100 * acc : 5.2f}")
