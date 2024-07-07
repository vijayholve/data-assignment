from .models import DataPoint
import json

def json_data():
    with open("data/jsondata.json", "r") as f:
        data=json.load(f)
        