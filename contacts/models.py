from datetime import datetime
from django.db import models

class Contact(models.Model):
    organization = models.CharField(max_length=200)
    organization_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank = False)
    contact_date = models.DateTimeField(default = datetime.now, blank=True)
    user_id = models.IntegerField(blank = True)

    def __str__(self):
        return self.name