import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
data = pd.read_csv('BTC-USD.csv', date_parser=True)
data.tail()
data_training = data[data['Date'] < '2020-01-01'].copy()

data_test = data[data['Date'] > '2020-01-01'].copy()
print(data_training)
training_data = data_training.drop(['Date','Open','Low','High','Volume', 'Adj Close'], axis=1)
print(training_data)
scaler = MinMaxScaler()
training_data = scaler.fit_transform(training_data)