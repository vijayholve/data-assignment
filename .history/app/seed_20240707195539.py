from .models import DataPoint
import json

def json_data():
    with open("data/jsondata.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file) 
        for item in data:
            obj=DataPoint.objects.create(
                end_year
intensity
sector
topic
insight
url
region
start_year
    impact = models.CharField(max_length=100, blank=True, null=True)
added
published
country
relevance
pestle
source
title
likelihood
city
            )
            