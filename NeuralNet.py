import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
Model = Sequential([
        Dense(128, activation='relu', input_shape=(784,)),
        Dense(128, activation='relu'),
        Dense(10, activation='softmax')
        ])


from keras import losses

Model.compile(loss=losses.mean_squared_error, 
              optimizer='sgd',
              metrics=['accuracy'])

Model.summary()
