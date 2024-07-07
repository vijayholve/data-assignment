from .models import DataPoint
import json
from datetime import datetime
def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%B, %d %Y %H:%M:%S")
    except ValueError:
        return None

def json_data():
    with open("data/jsondata.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
        for item in data:
            DataPoint.objects.create(
                end_year=item.get("end_year", ""),
                intensity=item.get("intensity", 0),
                sector=item.get("sector", ""),
                topic=item.get("topic", ""),
                insight=item.get("insight", ""),
                url=item.get("url", ""),
                region=item.get("region", ""),
                start_year=item.get("start_year", ""),
                impact=item.get("impact", ""),
                added=parse_date(item.get("added", "")),
                published=parse_date(item.get("published", "")),
                country=item.get("country", ""),
                relevance=item.get("relevance", 0),
                pestle=item.get("pestle", ""),
                source=item.get("source", ""),
                title=item.get("title", ""),
                likelihood=item.get("likelihood", 0),
                city=item.get("city", "")  # Handle city field if it's not already there
            )
           