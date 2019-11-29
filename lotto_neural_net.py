# WIP: This is not complete
#
# A script to train a model on previous winning lotto numbers
# and attempt use that model to predict future winning numbers

from numpy import loadtxt

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

# load the dataset
dataset = loadtxt('numbers_raw.csv', delimiter=',')

# split into input (X) and output (y) variables
X = dataset[:, 0:3]  # inputs: year, month, day
y = dataset[:, 3:9]  # outputs: 6 numbers, excluding bonus

# split into train and test
n_train = int(len(X) / 2)
trainX, testX = X[:n_train, :], X[n_train:, :]
trainy, testy = y[:n_train], y[n_train:]

# define the model
model = Sequential()
model.add(Dense(7, input_dim=3, activation='relu', kernel_initializer='he_uniform'))
model.add(Dense(7, activation='relu'))
model.add(Dense(6, activation='softmax'))

opt = SGD(lr=0.01, momentum=0.9)

# use categorical_crossentropy for multi-output problems
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

# fit model
model.fit(trainX, trainy, validation_data=(testX, testy), epochs=100, verbose=0)

# evaluate the model
_, train_acc = model.evaluate(trainX, trainy, verbose=0)
_, test_acc = model.evaluate(testX, testy, verbose=0)
print('Train: %.3f, Test: %.3f' % (train_acc, test_acc))
