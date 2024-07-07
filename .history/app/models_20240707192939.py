# app/models.py
from django.db import models
from django.utils import timezone

class DataPoint(models.Model):
    end_year = models.CharField(max_length=4, blank=True, null=True)
    intensity = models.IntegerField()
    sector = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    insight = models.TextField(default='No ')
    url = models.URLField()
    region = models.CharField(max_length=100)
    start_year = models.CharField(max_length=4, blank=True, null=True)
    impact = models.CharField(max_length=100, blank=True, null=True)
    added = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField()
    country = models.CharField(max_length=100)
    relevance = models.IntegerField()
    pestle = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    title = models.TextField()
    likelihood = models.IntegerField()
    city = models.CharField(max_length=100)  
