from .models import DataPoint
import json

def json_data():
    with open("/data/jsondata.json","r") as json_file:
        data=json.load(json_file)
        print(data)