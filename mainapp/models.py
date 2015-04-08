from django.contrib.auth.models import User
from django.db import models

# User's documents model
class Data(models.Model):
    user_id = models.ForeignKey(User, related_name='user')   # user id from User table
    data_name = models.CharField(max_length=64)              # name of document
    data_type = models.CharField(max_length=64)              # type of document Ex: .doc
    data_size = models.IntegerField()                        # size of document Mb
    #data_upload_time = models.DateField()                   # data uploaded date

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')