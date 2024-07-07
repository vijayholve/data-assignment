from .models import DataPoint
import json

def json_data():
    with open("data/jsondata.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file) 
        obj=dat
        