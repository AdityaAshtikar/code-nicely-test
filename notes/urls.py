from django.urls import path, include
from notes import views

urlpatterns = [
    path('', views.home, name='home'),
]
