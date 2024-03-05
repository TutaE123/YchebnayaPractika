from django.conf import settings
from django.db import models

class Koloda(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    наименование = models.CharField(max_length=200)
    описание = models.TextField()

class Cards(models.Model):
    лицо = models.TextField()
    изнанка = models.TextField() 