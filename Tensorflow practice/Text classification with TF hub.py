import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

print(f"\nVersion: {tf.__version__}")
print(f"Eager mode: {tf.executing_eagerly()}")
print(f"Hub version: {hub.__version__}\n")
print("GPU is, ", "available\n" if tf.config.experimental.list_physical_devices("GPU") else "NOT AVAILABLE\n")

train_data, val_data, test_data = tfds.load( # A dataset of movie reviews where each review is labelled 1 for positive and 0 for negative
    name = "imdb_reviews",
    split = ("train[:60%]", "train[60%:]", "test"),
    as_supervised = True
)

train_data_batch, y_train_batch = next(iter(train_data.batch(10)))
print(f"\n{train_data_batch}\n{y_train_batch}\n")

# To represent text for the neural network I am going to use a pre-trained text embedding model from TF Hub
embedding = "https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim/1" # Name of model is starting from google/
hub_layer = hub.KerasLayer(embedding, input_shape = [], dtype = tf.string, trainable = True) # No matter the length of the input text the output shape is always (num_examples, embedding_dimension)

"""
The pre-trained model splits the sentences into tokens, embeds each token and then combines the embeddings
"""

model = Sequential([
    hub_layer,
    Dense(16, activation = "relu"),
    Dense(1)
])

model.summary()

loss_fn = tf.keras.losses.BinaryCrossentropy(from_logits = True)
model.compile(optimizer = "adam", loss = loss_fn, metrics = ["accuracy"])

print("\n")
history = model.fit(train_data.shuffle(10000).batch(512), epochs = 20, validation_data = val_data.batch(512), verbose = 1)
print("\n")

loss, accuracy = model.evaluate(test_data.batch(512), verbose = 0)
print(f"\nTest loss: {loss}. Test accuracy: {accuracy}")

history_dict = history.history
accuracy = history_dict["accuracy"]
val_accuracy = history_dict["val_accuracy"]
loss = history_dict["loss"]
val_loss = history_dict["val_loss"]
epochs = range(1, len(accuracy) + 1)

plt.plot(epochs, loss, "bo", label = "Training loss") # bo means blue dot
plt.plot(epochs, val_loss, "b", label = "Validation_loss") # b means solid blue line
plt.title("Training and Validation_loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.show()

plt.clf()   # clear figure
plt.plot(epochs, accuracy, 'bo', label='Training acc')
plt.plot(epochs, val_accuracy, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()
