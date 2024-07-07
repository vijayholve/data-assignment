from .models import DataPoint


def json_data():
    with open("data.jsondata.json","r") as json_file:
        data=js