import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv('BTC-USD.csv', date_parser=True)
data_training = data[data['Date'] < '2020-01-01'].copy()
data_test = data[data['Date'] < '2020-01-01'].copy()
training_data = data_training.drop(['Date', 'Adj Close'], axis=1)

scaler = MinMaxScaler()
training_data = scaler.fit_transform(training_data)

X_train = []
Y_train = []

for i in range(90, training_data.shape[0]):
    X_train.append(training_data[i - 90:i])

    Y_train.append(training_data[i, 0])

X_train, Y_train = np.array(X_train), np.array(Y_train)

from tensorflow.keras import Sequential

from tensorflow.keras.layers import Dense, LSTM, Dropout

model = Sequential()
model.add(LSTM(units=50, activation='relu', return_sequences=True, input_shape=(X_train.shape[1], 5)))

model.add(Dropout(0.2))
model.add(LSTM(units=60, activation='relu', return_sequences=True))

model.add(Dropout(0.3))
model.add(LSTM(units=80, activation='relu', return_sequences=True))

model.add(Dropout(0.4))
model.add(LSTM(units=120, activation='relu'))

model.add(Dropout(0.5))
model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')

history = model.fit(X_train, Y_train, epochs=20, batch_size=50, validation_split=0.1)

loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(len(loss))
plt.figure()
plt.plot(epochs, loss, 'b', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
plt.title("Training and Validation Loss")
plt.legend()
plt.show()

part_60_days = data_training.tail(60)
df = part_60_days.append(data_test, ignore_index=True)
df = df.drop(['Date', 'Adj Close'], axis=1)

inputs = scaler.transform(df)

X_test = []

Y_test = []

for i in range(90, inputs.shape[0]):
    X_test.append(inputs[i - 90:i])
    Y_test.append(inputs[i, 0])

    X_test, Y_test = np.array(X_test), np.array(Y_test)

    Y_pred = model.predict(X_test)
print(X_test)