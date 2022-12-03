from django.db import models

# Create your models here.

class rent_rem(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    dob = models.DateField()
    rent_amount = models.IntegerField()
    due_date = models.DateField()
    tenent_email = models.CharField(max_length=122)
    tenent_phone = models.IntegerField()
    tmessage = models.CharField(max_length=300)