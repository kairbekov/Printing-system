from django.db import models

# Users
class Person(models.Model):
    first_name = models.CharField(max_length=30)      # Name
    last_name = models.CharField(max_length=30)       # Surname
    email = models.CharField(max_length=30)           # Email
    balance = models.IntegerField()                   # current balance
    printed = models.IntegerField()                   # count of printed papers

