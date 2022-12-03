from django.db import models

# Create your models here.

class test(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    age = models.IntegerField()
    # your_email = models.CharField(max_length=122)
    dob = models.DateField()
    rent = models.IntegerField()
    due_date = models.DateField()
    tenent_email = models.CharField(max_length=122)
    tenent_phone = models.IntegerField()
    tmessage = models.TextField()