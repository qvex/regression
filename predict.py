import os
import django
import csv 
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'regression.settings')
django.setup()

from regressionApp.models import CropPrediction, PredYear, PredPrice, PrevYear, PrevPrice

years = []
crops = []
cropPrices = {}

def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        rowCount = 0
        for row in csvFileReader:
            if rowCount == 0:
                for i in range(1, 6):
                    years.append(row[i])
                rowCount += 1
            else:
                yearDict = {}
                for i in range(len(years)):
                    
                    yearDict[years[i]] = row[i + 1]    
                    cropPrices[row[0]] = yearDict               
            

def predict_price(years, prices, requestedYear):
    linear_mod = linear_model.LinearRegression()

    years = np.reshape(years,(len(years), 1))
    prices = np.reshape(prices,(len(prices), 1))
    linear_mod.fit(years, prices)
    predicted_price = linear_mod.predict(requestedYear)
    return predicted_price[0][0], linear_mod.coef_[0][0], linear_mod.intercept_[0]
