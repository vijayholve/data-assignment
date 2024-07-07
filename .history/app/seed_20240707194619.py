from .models import DataPoint
import json

def json_data():
    json_file=open("data/jsondata")

    data = json.load(json_file)
        