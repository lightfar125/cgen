import numpy as np
from pandas import read_csv
from keras.models import Sequential
from keras.layers.core import Dense
from keras.layers.recurrent import LSTM

path = 'data/2020.csv'
COLS = [0, 1, 2, 3, 4, 5, 6]

# load the dataset
data = read_csv(path, header=0, index_col=0, usecols=COLS)


def _load_data(df, n_prev=100):
    docX, docY = [], []
    for i in range(len(df) - n_prev):
        docX.append(df.iloc[i:i + n_prev].values)
        docY.append(df.iloc[i + n_prev].values)
    alsX = np.array(docX)
    alsY = np.array(docY)
    return alsX, alsY


def train_test_split(df, test_size=0.1):
    num_train = round(len(df) * (1 - test_size))
    X_train, y_train = _load_data(df.iloc[0:num_train])
    X_test, y_test = _load_data(df.iloc[num_train:])
    return X_train, y_train, X_test, y_test


model = Sequential()
model.add(LSTM(49, input_shape=(None, 6)))
model.add(Dense(6, input_dim=49))
model.compile(loss="mse", optimizer="adam")

X_train, y_train, X_test, y_test = train_test_split(data)

model.fit(X_train, y_train, batch_size=450, epochs=3, validation_split=0.05)

predicted = model.predict(X_test)
rmse = np.sqrt(((predicted - y_test) ** 2).mean(axis=0))

print(f"\nPredicted numbers: {np.around(rmse)}")
