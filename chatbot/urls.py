from django.urls import path

from . import views

urlpatterns = [
    path('ask/', views.ask, name='ask'),
    path('join/', views.join, name='join'),
    path('crawl/', views.crawl, name='crawl'),
    path('calendar/', views.calendar, name='calendar')
]