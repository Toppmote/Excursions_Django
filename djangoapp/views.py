from django.shortcuts import render


def loadStartPage(request):
    return render(request, 'djangoapp/index.html')


def loadAboutPage(request):
    return render(request, 'djangoapp/about.html')
