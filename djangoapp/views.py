from django.shortcuts import render, redirect
from .models import *
from .forms import *


def loadStartPage(request):
    return render(request, 'djangoapp/index.html')


def loadAboutPage(request):
    return render(request, 'djangoapp/about.html')


def loadCitiesPage(request):
    cities = City.objects.order_by('name')
    return render(request, 'djangoapp/cities.html', {'cities': cities})


def loadCityPage(request, city_id):
    city = City.objects.get(pk=city_id)
    return render(request, 'djangoapp/city_details.html', {'city': city})


def loadExcursionsPage(request):
    if request.method == 'POST':
        form = ExcursionForm(request.POST)
        if form.is_valid():
            form.save()

    excursions = Excursion.objects.order_by('name')
    form = ExcursionForm()
    return render(request, 'djangoapp/excursions.html', {'excursions': excursions, 'form': form})


def loadExcursionPage(request, excursion_id):
    if request.method == 'POST':
        excursion_from_db = Excursion.objects.get(pk=excursion_id)
        form = ExcursionForm(request.POST, instance=excursion_from_db)
        if form.is_valid():
            form.save()

    excursion = Excursion.objects.get(pk=excursion_id)
    form = ExcursionForm()
    return render(request, 'djangoapp/excursion_details.html',
                  {'excursion': excursion, 'form': form})


def deleteExcursion(request, excursion_id):
    try:
        record = Excursion.objects.get(id=excursion_id)
        record.delete()
        print("Excursion deleted successfully!")
    except:
        print("Excursion doesn't exists")
    return redirect('excursions_page')
