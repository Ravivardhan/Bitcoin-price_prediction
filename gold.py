from sklearn.linear_model import LinearRegression
import datetime as dt
import pandas as pd
# pandas and numpy are used for data manipulation
import pandas as pd
import numpy as np

# matplotlib and seaborn are used for plotting graphs
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

# yahoo finance is used to fetch data
import yfinance as yf

Df = yf.download('BTC-USD', '2021-01-01', '2021-06-01', auto_adjust=True)

# Only keep close columns
Df = Df[['Close']]

Df = Df.dropna()




old = yf.download('BTC-USD', '2021-01-01', '2021-06-01', auto_adjust=True)

    # Only keep close columns
old = Df[['Close']]

    # Drop rows with missing values
old = Df.dropna()

    # Plot the closing price of GLD
old.Close.plot(figsize=(10, 7), color='r')
plt.ylabel("bitcoin  Prices")
plt.title("bitcoin Price Series")
plt.show()



Df['S_3'] = Df['Close'].rolling(window=3).mean()
Df['S_9'] = Df['Close'].rolling(window=9).mean()
Df['next_day_price'] = Df['Close'].shift(-1)

Df = Df.dropna()
X = Df[['S_3', 'S_9']]

# Define dependent variable
y = Df['next_day_price']

t = .4
t = int(t*len(Df))

# Train dataset
X_train = X[:t]
y_train = y[:t]

# Test dataset
X_test = X[t:]
y_test = y[t:]

linear = LinearRegression().fit(X_train, y_train)

predicted_price = linear.predict(X_test)

##################################################################################################





import pandas as pd
import numpy as np
from datetime import datetime, timedelta

date_today = datetime.now()
days = pd.date_range(date_today, date_today + timedelta(85), freq='D')

np.random.seed(seed=1111)
data = np.random.randint(1, high=100, size=len(days))
df = pd.DataFrame({'test': days, 'col2': data})
df = df.set_index('test')



##################################################################################################


predicted_price = pd.DataFrame(
    predicted_price, index=df.index, columns=['price'])
predicted_price.plot(figsize=(10, 7))

plt.legend(['predicted_price'])
plt.ylabel("BTC-USD Price")
plt.show()



