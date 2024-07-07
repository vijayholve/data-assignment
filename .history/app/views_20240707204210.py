from django.shortcuts import render
from .models import DataPoint
def home(request):
    data=DataPoint.objects.all()
    context={"data"}
    return render(request,"base/home.html")

