from django.db import models
from django.db.models.deletion import CASCADE
from django.core.urlresolvers import reverse

class Menu(models.Model):

    name = models.CharField(max_length = 250)
    image = models.FileField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Detail(models.Model):

    menu = models.ForeignKey(Menu, on_delete = models.CASCADE)
    name = models.CharField(max_length = 250)
    price = models.IntegerField(default = 0)
    size = models.CharField(max_length = 50)
    image = models.FileField(null=True, blank=True)
    
    def __str__(self):
        return self.name + '-' + self.size