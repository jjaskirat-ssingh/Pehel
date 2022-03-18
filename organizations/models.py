from django.db import models
from datetime import datetime

class Organization(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100, default='pehel@gmail.com')
    objective = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_joined = models.DateField(blank=True)
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=False)
    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    display = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name