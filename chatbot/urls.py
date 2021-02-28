from django.urls import path

from . import views

urlpatterns = [
    path('ask/', views.ask, name='ask'),
    path('crawl/', views.crawl, name='crawl'),
]