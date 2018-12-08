import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from testing_callback import TestCallback

df = pd.read_csv('modified_datasets/processed_user_onehot.csv')

# splits data set by sampling randomly
train_data=df.sample(frac=0.8,random_state=200)
test_data=df.drop(train_data.index)

train_labels = train_data.country_destination
test_labels = test_data.country_destination

train_data = train_data.drop(columns=['country_destination'])
test_data = test_data.drop(columns=['country_destination'])

# convert labels to one-hot
d = {'NDF':0, 'Booked':1}
train_labels = train_labels.map(d)
test_labels = test_labels.map(d)
train_labels = keras.utils.to_categorical(train_labels, num_classes=2)
test_labels = keras.utils.to_categorical(test_labels, num_classes=2)


model = keras.Sequential()
model.add(keras.layers.Dense(128, activation=tf.nn.relu, input_dim=149))
# model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(256, activation=tf.nn.relu))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(256, activation=tf.nn.relu))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(128, activation=tf.nn.relu))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(2, activation=tf.nn.softmax))

# model.add(keras.layers.Dense(128, activation=tf.nn.sigmoid, input_dim=132))
# # model.add(keras.layers.Dropout(0.2))
# model.add(keras.layers.Dense(256, activation=tf.nn.sigmoid))
# model.add(keras.layers.Dropout(0.2))
# model.add(keras.layers.Dense(256, activation=tf.nn.sigmoid))

# model.add(keras.layers.Dense(2, activation=tf.nn.softmax))


# sgd = keras.optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
							optimizer=tf.train.AdamOptimizer(),
							metrics=['accuracy'])

tb_callback = keras.callbacks.TensorBoard(log_dir='./Graph', histogram_freq=0, write_graph=True, write_images=True)
test_cb =  TestCallback((test_data, test_labels))

model.fit(train_data, train_labels, epochs=10, batch_size=10, callbacks = [tb_callback, test_cb])

# score = model.evaluate(test_data, test_labels)
# print('score = ' + str(score))

#model.fit(train_images, train_labels, epochs=5)

# for col in df.columns:
# 	df[col] = pd.Categorical(df[col], categories=df[col].unique()).codes