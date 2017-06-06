from __future__ import unicode_literals

from django.db import models

class Map_location(models.Model):
    place = models.CharField(max_length = 250)
    latitude = models.FloatField(default = 28.600005)
    longitude = models.FloatField(default = 77.346965)
    
    def __str__(self):
        return str(self.latitude)