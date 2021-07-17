'''import pandas as pd
import pandas_datareader.data as pdr
import datetime as dt
from datetime import date
from datetime import date, timedelta
from matplotlib import pyplot as pt

days_before = (date.today()-timedelta(days=90)).isoformat()
start = days_before
days_before2 = (date.today()-timedelta(days=1)).isoformat()
end = days_before2
print(start)
print(end)

df = pdr.DataReader('BTC-USD','yahoo',start,end)
df['date'] = pd.date_range(start=start, periods=len(df))
pt.plot(df.date,df.Close)
pt.xlabel("Last 3 months")
pt.ylabel("Price in usd")
pt.grid(True)
pt.tight_layout()
pt.show()'''

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

