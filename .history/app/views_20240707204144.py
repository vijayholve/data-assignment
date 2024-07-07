from django.shortcuts import render
from .models import DataPoint
def home(request):
    return render(request,"base/home.html")

