from tensorflow import keras

class TestCallback(keras.callbacks.Callback):
    def __init__(self, test_data):
        self.test_data = test_data

    def on_epoch_end(self, epoch, logs={}):
        data, label = self.test_data
        loss, acc = self.model.evaluate(data, label, verbose=0)
        print('\nTesting loss: {}, acc: {}\n'.format(loss, acc))