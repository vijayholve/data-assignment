from .models import DataPoint
import json
from datetime import datetime
from django.utils import timezone 

def parse_date(date_str):
    try:
        naive_dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        aware_dt = timezone.make_aware(naive_dt, timezone=timezone.utc)
        return aware_dt
    except ValueError:
        return None

def json_data():
    with open("data/jsondata.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
        for item in data:
            try:
                intensity = int(item.get("intensity", 0))
                relevance = int(item.get("relevance", 0))
                likelihood = int(item.get("likelihood", 0))
            except ValueError:
                intensity = 0
                relevance = 0
                likelihood = 0
            
            DataPoint.objects.create(
                end_year=item.get("end_year", ""),
                intensity=intensity,
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
                relevance=relevance,
                pestle=item.get("pestle", ""),
                source=item.get("source", ""),
                title=item.get("title", ""),
                likelihood=likelihood,
                city=item.get("city", "")
            )