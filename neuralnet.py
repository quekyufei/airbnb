import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('numerical_cat_no_actions.csv')
cols = list(df)
data = df.drop(columns=['country_destination'])
labels = df.country_destination
d = {'NDF':0, 'Booked':1}
labels = labels.map(d)
labels = keras.utils.to_categorical(labels, num_classes=2)

train = data

model = keras.Sequential()
# model.add(keras.layers.Dense(128, activation=tf.nn.relu, input_dim=132))
# # model.add(keras.layers.Dropout(0.2))
# model.add(keras.layers.Dense(256, activation=tf.nn.relu))
# model.add(keras.layers.Dropout(0.2))
# model.add(keras.layers.Dense(256, activation=tf.nn.relu))
# model.add(keras.layers.Dropout(0.2))
# model.add(keras.layers.Dense(128, activation=tf.nn.relu))
# model.add(keras.layers.Dropout(0.2))
# model.add(keras.layers.Dense(2, activation=tf.nn.softmax))

model.add(keras.layers.Dense(32, activation=tf.nn.sigmoid, input_dim=15))
# model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(32, activation=tf.nn.sigmoid))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(32, activation=tf.nn.sigmoid))

model.add(keras.layers.Dense(32, activation=tf.nn.sigmoid))

model.add(keras.layers.Dense(32, activation=tf.nn.sigmoid))

model.add(keras.layers.Dense(32, activation=tf.nn.sigmoid))

model.add(keras.layers.Dense(32, activation=tf.nn.sigmoid))

model.add(keras.layers.Dense(32, activation=tf.nn.sigmoid))

model.add(keras.layers.Dense(32, activation=tf.nn.sigmoid))

model.add(keras.layers.Dense(32, activation=tf.nn.sigmoid))

model.add(keras.layers.Dense(32, activation=tf.nn.sigmoid))

model.add(keras.layers.Dense(32, activation=tf.nn.sigmoid))

model.add(keras.layers.Dense(2, activation=tf.nn.softmax))


# sgd = keras.optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
							optimizer=tf.train.AdamOptimizer(),
							metrics=['accuracy'])

tb_callback = keras.callbacks.TensorBoard(log_dir='./Graph', histogram_freq=0, write_graph=True, write_images=True)

model.fit(data, labels, epochs=10, batch_size=10, callbacks = [tb_callback])

#model.fit(train_images, train_labels, epochs=5)

# for col in df.columns:
# 	df[col] = pd.Categorical(df[col], categories=df[col].unique()).codes