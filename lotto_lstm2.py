import numpy as np

from pandas import read_csv
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout, Flatten
from keras.layers.recurrent import LSTM

# load the dataset
data = read_csv('data/numbers.csv', header=0, index_col=0, usecols=[0, 1, 2, 3, 4, 5, 6])

X = data.values
train_size = int(len(X) * 0.99)
train, test = X[0:train_size], X[train_size:len(X)]
print('Observations: %d' % (len(X)))
print('Training Observations: %d' % (len(train)))
print('Testing Observations: %d' % (len(test)))

train = np.reshape(train, (train.shape[0], 1, train.shape[1]))
test = np.reshape(test, (test.shape[0], 1, test.shape[1]))

model = Sequential()
model.add(LSTM(input_shape=(1, 6), units=50))
# model.add(Dropout(.2))
# model.add(Flatten())
model.add(Dense(input_dim=50, units=6))
model.compile(loss="mean_squared_error", optimizer="rmsprop")



# and now train the model
# batch_size should be appropriate to your memory size
# number of epochs should be higher for real world problems
model.fit(train, test, epochs=1)

# predicted = model.predict(X)

# print(predicted)
# rmse = np.sqrt(((predicted - y_test) ** 2).mean(axis=0))


