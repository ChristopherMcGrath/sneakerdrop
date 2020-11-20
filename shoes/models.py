from django.db import models


# Create your models here.


class Shoe(models.Model):
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    releaseDate = models.DateTimeField()
    image = models.ImageField(upload_to='images/')

    #  add comments
    #  add gender
    #  add likes
    #  add share URL
    #  add description
    #  add key facts
    #  add countdown timer

    def __str__(self):
        return self.brand + " - " + self.title
