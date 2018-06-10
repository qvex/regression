import os
import django
import csv 
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import panda as pd
import statsmodels as alias sm

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

def show_plot(years, prices):
    linear_mod = linear_model.LinearRegression()
    years = np.reshape(years, (len(years), 1))
    prices = np.reshape(prices, (len(prices), 1))
    linear_mod.fit(years, prices)

    plt.scatter (years, prices, color = 'green')
    plt.plot(years, linear_mod.predict(years), color = 'red', linewidth = 3)
    plt.show()
    return

    def queryCropPrediction(crop, dataset):
        found = False
    cropPred = CropPrediction.objects.get_or_create(cropName = crop.lower())[0]
    cropPred.save()
    for key, value in dataset.items():
        if crop.lower() == key.lower():
            found = True
            yr = []
            pr = []
            for k, v in value.items():
                yr.append(k)
                pr.append(v)
                
                pdYr = PredYear.objects.get_or_create(year = k)[0]
                pdYr.save()
                cropPred.predYears.add(pdYr)

                pdPr = PredPrice.objects.get_or_create(price = v)[0]
                pdPr.save()
                cropPred.predPrices.add(pdPr)

    if (not found):
        print(crop, "not found")
     
get_data('crop_price_details.csv')

predictedCropPrices = {}

next_five_prices = []
next_years = [2017, 2018, 2019, 2020, 2021]

for key, value in cropPrices.items():
    yearVals = {}
    for year in next_years:
        yr = []
        pr = []
        for k, v in value.items():
            yr.append(k)
            pr.append(v)
        yearVals[year] = round(predict_price(yr, pr, year)[0], 2)
        #print(value.values())
    
    predictedCropPrices[key] = yearVals

for key, value in predictedCropPrices.items():
    queryCropPrediction(key, predictedCropPrices)
print (key,"added")

def run_ordinary_least_squares(ols_dates, ols_data, statsmodels_settings):
    
        intercept = np.column_stack((ols_dates, ols_dates ** statsmodels_settings.exponent))
        constant = sm.add_constant(intercept)
        statsmodel_regression = sm.OLS(ols_prices, constant).fit()
        print(statsmodel_regression.summary())
        if statsmodels_settings.confidence:
            prstd, lower, upper = wls_prediction_std(statsmodel_regression)
            return statsmodel_regression, lower, upper
        else:
return statsmodel_regression