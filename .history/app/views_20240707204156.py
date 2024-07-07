from django.shortcuts import render
from .models import DataPoint
def home(request):
    data=DataPoint.objects
    return render(request,"base/home.html")

