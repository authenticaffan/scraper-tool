# scraper/urls.py
from django.urls import path
from .views import index, scrape_website

urlpatterns = [
    path('', index, name='index'),
    path('scrape/', scrape_website, name='scrape_website'),
]
