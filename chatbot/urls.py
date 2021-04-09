from django.urls import path

from . import views

urlpatterns = [
    path('answer/', views.answer),
    path('user/', views.user),
    path('usercourse/', views.usercourse),
]