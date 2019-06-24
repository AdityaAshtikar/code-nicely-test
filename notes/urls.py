from django.urls import path, include
from notes import views

urlpatterns = [
    path('', views.home, name='home'),
    path('showPeople', views.showPeople, name='showPeople'),
]
