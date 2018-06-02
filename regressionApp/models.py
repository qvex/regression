from django.db import models
import ast
# Create your models here.

DEAFULT_VAL = 1

class PrevPrice(models.Model):
    price = models.FloatField()

class PrevYear(models.Model):
    year = models.CharField(max_length = 15)

class PredPrice(models.Model):
    price = models.FloatField()

class PredYear(models.Model):
    year = models.CharField(max_length = 15)

class CropPrediction(models.Model):
    cropName = models.CharField(max_length = 150, unique = True)
    
    prevYears = models.ManyToManyField(PrevYear, default = DEAFULT_VAL)
    prevPrices = models.ManyToManyField(PrevPrice, default = DEAFULT_VAL)

    predYears = models.ManyToManyField(PredYear, default = DEAFULT_VAL, related_name = 'predYears_set')
    predPrices = models.ManyToManyField(PredPrice, default = DEAFULT_VAL)

