from django.db import models

# Create your models here.
class savedata(models.Model):
    username = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length = 256, default="")
