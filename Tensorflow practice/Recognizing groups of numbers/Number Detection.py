import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Sequential
import numpy as np

dataset = np.genfromtxt("train.csv")
print(dataset)

"""
meh = tf.reshape(dataset[0], (300, 302))

import matplotlib.pyplot as plt
plt.imshow(meh[0:100], cmap = "gray")
plt.show()
"""
