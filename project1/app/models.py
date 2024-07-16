from django.db import models

class urunler(models.Model):
    title = models.CharField(max_length= 50)
    description = models.CharField(max_length= 400)
    image =models.ImageField()


class referanslarimiz(models.Model):
    title = models.CharField(max_length= 50)
    description = models.CharField(max_length= 400)
    image =models.ImageField()