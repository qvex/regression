from django.shortcuts import render
from .models import CropPrediction
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    prices = CropPrediction.objects.all()
    return render(request, 'regressionApp/index.html', {'price' : prices})

def crop_data(request):
    crop_name = request.POST.get('crop_name')
    crop = CropPrediction.objects.filter(cropName = crop_name)[0]

    crops = CropPrediction.objects.all()

    crop.cropName = crop.cropName.title()

    predicted_prices = crop.predPrices.all()
    predicted_years = crop.predYears.all()

    return render(request, 'regressionApp/crop_data.html', {'prices' : predicted_prices, 'years' : predicted_years, 'crop' : crop, 'price' : crops})
