import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Softmax, Dropout

gpu_options = tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction = 0.3)
sess = tf.compat.v1.Session(config = tf.compat.v1.ConfigProto(gpu_options = gpu_options))
tf.keras.backend.set_floatx("float64")
print(f"\nTensorflow version: {tf.__version__}")

fashion_mnist = keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print(f"images shape: {x_train.shape}\n")

# Showing the first image and seeing the range of values the pixels take
plt.figure()
plt.imshow(x_train[0])
plt.colorbar()
plt.grid(False)
plt.show()

x_train, x_test = x_train / 255.0, x_test / 255.0 # Each image takes a value between 0 - 255 for each pixel so this will normalize the dataset

# Checking that the data is in the correct format:
plt.figure(figsize = (10, 10))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_train[i], cmap = plt.cm.binary)
    plt.xlabel(class_names[y_train[i]])
plt.show()

model = Sequential([
    Flatten(input_shape = (28, 28)),
    Dense(128, activation = "relu"),
    Dropout(0.2),
    Dense(10)
])

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True)

model.compile(optimizer = "adam",
              loss = loss_fn,
              metrics = ["accuracy"]
)

print("\n")
model.fit(x_train, y_train, epochs = 10)

eval_loss, eval_acc = model.evaluate(x_test, y_test, verbose = 0)
print(f"\nEvaluation accuracy: {eval_acc}. Evaluation_loss: {eval_loss}")

probability_model = Sequential([
    model,
    Softmax()
])

prediction = probability_model.predict(x_test[:1])
label = y_test[:1][0]
print(f"\nProbability model prediction: {np.argmax(prediction)}, actual label: {label}")
