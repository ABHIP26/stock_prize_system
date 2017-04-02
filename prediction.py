import math
from datetime import datetime as ds
import time
import matplotlib.pyplot as plt
import numpy as np
#import quandl
from matplotlib import style
from numba.tests.test_array_constants import dt
from sklearn import preprocessing, cross_validation
from sklearn.linear_model import LinearRegression
import pandas as pd
style.use('ggplot')

#df = quandl.get("WIKI/GOOGL")

import pandas as pd
import csv

df = pd.read_csv('C:\Users\Lenovo\Desktop\PycharmProjects\stock_prize_system\input.csv')


df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
forecast_col = 'Adj. Close'
df.fillna(value=-99999, inplace=True)
forecast_out = int(math.ceil(0.01 * len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)

X = np.array(df[['Adj. Volume','HL_PCT','PCT_change']])
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)

y = np.array(df['label'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print(confidence*100)
forecast_set = clf.predict(X_lately)
df['Forecast'] = np.nan


df['Date'] = df['Date'].apply(dt.datetime.strptime,args=("%Y-%m-%d",))
df.set_index(df['Date'], inplace=True)
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 864000
next_unix = last_unix + one_day
for i in forecast_set:
    next_unix += one_day
    next_date=next_unix
    df.loc[next_date]= [np.nan for _ in range(len(df.columns)-1)]  + [i]

for i in forecast_set:
    next_date = ds.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns) - 1)] + [i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
