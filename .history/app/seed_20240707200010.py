from .models import DataPoint
import json

def json_data():
    with open("data/jsondata.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file) 
        for item in data:
            pr
            obj=DataPoint.objects.create(
                end_year=item.get("end_year", ""),
                intensity=item.get("intensity", 0),
                sector=item.get("sector", ""),
                topic=item.get("topic", ""),
                insight=item.get("insight", ""),
                url=item.get("url", ""),
                region=item.get("region", ""),
                start_year=item.get("start_year", ""),
                impact=item.get("impact", ""),
                added=item.get("added", ""),
                published=item.get("published", ""),
                country=item.get("country", ""),
                relevance=item.get("relevance", 0),
                pestle=item.get("pestle", ""),
                source=item.get("source", ""),
                title=item.get("title", ""),
                likelihood=item.get("likelihood", 0),
                city=item.get("city", "")
                )
            obj.save()