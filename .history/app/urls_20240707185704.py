from django.urls import path, include
from .views import *
urlpatterns = [
    path('add/', add),
    path('<int:id>/edit/', edit)