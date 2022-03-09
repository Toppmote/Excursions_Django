from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.loadStartPage, name='start_page'),
    path('about', views.loadAboutPage, name='about_page'),
    path('cities', views.loadCitiesPage, name='cities_page'),
    path('city/<city_id>', views.loadCityPage),
    path('excursions', views.loadExcursionsPage, name='excursions_page'),
    path('excursion/<excursion_id>', views.loadExcursionPage),
    path('excursion/delete/<excursion_id>', views.deleteExcursion),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
