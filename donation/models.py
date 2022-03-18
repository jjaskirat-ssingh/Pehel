from datetime import datetime
from django.db import models

class Donation(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField(blank = False)
    remarks = models.TextField(blank = False)
    #pikup_date = models.DateTimeField(default = 'NULL', blank=True)
    user_id = models.IntegerField(blank = True)

    def __str__(self):
        return self.name