from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=20 , default = "guest")
    pw = models.CharField(max_length= 12, default= "0000")
    