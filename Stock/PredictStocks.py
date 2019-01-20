#Predicting stocks utilizing ML  https://www.youtube.com/watch?v=SSu00IRRraY

import numpy as np 
import csv
from sklearn.svm import SVR
import matplotlib.pyplot as plt 

dates = []
prices = []

#getting the necessary data from a csv file
def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            #append the necessary info around the date (day) and open price (change according to what data you want)
            dates.append(int(row[0].split('-')[2]))
            prices.append(float(row[1]))

    #print date just to understand what is happening       
    print(dates)
    return

def predict_prices(dates, prices, x):
    #creating a 1  dimensional array for elements
    dates = np.reshape(dates, (len(dates), 1))

#linear, polynomial and rbf(radio base function) type graphs, C=1e3 is a sicentific notation = 1000
    svr_lin = SVR(kernel='linear', C=1e3)
    svr_poly = SVR(kernel='poly', C=1e3, degree=2)
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    svr_lin.fit(dates, prices)
    svr_poly.fit(dates, prices)
    svr_rbf.fit(dates, prices)

#plotting all necessary information to understand what is happening
    plt.scatter(dates, prices, color='black', label='Data')
    plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
    plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear model')
    plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial model')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()

    print('Showing graph')

#return predicted values for each SVR method
    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

get_data('Stock/MSFT.csv')

predictedprice = predict_prices(dates, prices, 29)