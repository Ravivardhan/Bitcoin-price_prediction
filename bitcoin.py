import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
import calendar
import time

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense,Dropout,LSTM
from tensorflow.keras.models import Sequential
from sklearn.linear_model import LinearRegression

# pandas and numpy are used for data manipulation
import datetime

today = datetime.date.today()

days=[]
days.append(today.strftime('%Y%m%d'))

for i in range(92):
    yesterday = today - datetime.timedelta(days=1)
    days.append(yesterday.strftime('%Y%m%d'))
    print(yesterday)
    today=yesterday
days=days[::-1]




import pandas_datareader as web
import datetime as dt

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense,Dropout,LSTM
from tensorflow.keras.models import Sequential
# matplotlib and seaborn are used for plotting graphs
import matplotlib.pyplot as plt

plt.style.use('seaborn-darkgrid')

# yahoo finance is used to fetch data

crypto_currency='BTC'
against_currency='USD'


start=dt.datetime(2021,3,2,)
end=dt.datetime.now()
try:
    Df=web.DataReader(f'{crypto_currency}-{against_currency}', 'yahoo' ,start,end)
except ConnectionError as c:
    print(c)

df=pd.DataFrame(Df)

dates=np.array(days).reshape((-1,1))
values=np.array(Df['Close'])



model=LinearRegression()
model.fit(dates,values)
print(model.predict(np.array([20210814]).reshape((-1,1))))


