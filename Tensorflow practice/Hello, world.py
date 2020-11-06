import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Dropout, Softmax
import numpy as np

tf.keras.backend.set_floatx("float64")
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0  # Images have grayscale values from 0 - 255 so this will normalize the dataset

model = Sequential([
    Flatten(input_shape = (28, 28)),  # Images are a 2D array of 28 by 28 values and so this will flatten it for the Dense layer
    Dense(128, activation = "relu"),
    Dropout(0.2), # 20% of the neurons will be ignored at random for each prediction to prevent overfitting
    Dense(10) # Output layer it will return a vector of "logits" or "log-odds" for each class, the closer to one the value the more confident the network is in it's prediction
])
# The reason you do not add an activation function of softmax to the last layer is because it is impossible to provide and exact and numerically stable loss calculation if using softmax in the last layer

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True) # Returns a scalar loss for each example

model.compile(optimizer = "adam",
              loss = loss_fn,
              metrics = ["accuracy"]
)

print("\n") # I am using cmd to execute the program so this will just make it easier to see the relevant information
model.fit(x_train, y_train, epochs = 5)

eval_loss, eval_acc = model.evaluate(x_test, y_test, verbose = 0)
print(f"\nEvaluation accuracy: {eval_acc}. Evaluation_loss: {eval_loss}")

#if you want to output probabilities then you can create another model like so:
probability_model = Sequential([
    model,
    Softmax()
])

prediction = probability_model.predict(x_test[:1])
label = y_test[:1][0]
print(f"\nProbability model prediction: {np.argmax(prediction)}, actual label: {label}")
