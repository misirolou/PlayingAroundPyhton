#Visualising stocks: https://www.youtube.com/watch?v=_T0l015ecK4
#learning some simple machine learning algorithms to help in prediction modelling
#monte-carlo simulation using stock to play around with this

import pandas_datareader.data as web
import pandas as pd 
import datetime as dt
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import style

style.use('ggplot')

start = dt.datetime(2018, 1, 3)
end = dt.datetime(2018, 11, 20)

#Microsoft stock using data reader pandas library to receive info, not stable at the time
#dependent on pandas_datareader.data version 0.7
prices = web.DataReader('MSFT', 'google', start, end)['Close']
returns = prices.pct_change()

last_price = prices[-1]

#number of simulations
num_simulations = 1000
num_days = 252

simultaion_df = pd.DataFrame()

#Doing the various simulations according to info provided
for x in range(num_simulations):
    count = 0
    daily_vol = returns.std()

    prices_series = []
    price = last_price * (1 + np.random.normal(0, daily_vol))
    prices_series.append(price)

    for y in range(num_days):
        if count == 251:
            break
        price = prices_series[count] * (1 + np.random.normal(0, daily_vol))
        prices_series.append(price)
        count += 1

    simultaion_df[x] = prices_series

#show a graph with all necessary inforamation, will try to do this in Jupyter notebook
fig = plt.figure()
fig.suptitle('Monte Carlo Simulation for Microsft Stock')
plt.plot(simultaion_df)
plt.axhline(y = last_price, color = 'r', linestyle = '-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()

