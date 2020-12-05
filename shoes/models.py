from django.db import models
from datetime import date


# Create your models here.


class Shoe(models.Model):
    title = models.CharField(max_length=255)
    nk = 'Nike'
    nb = 'New Balance'
    a = 'Adidas'
    ua = 'Under Armor'
    brand_CHOICES = (
        (nk, 'Nike'),
        (nb, 'New Balance'),
        (a, 'Adidas'),
        (ua, 'Under Armor'),
    )
    brand = models.CharField(max_length=100, choices=brand_CHOICES)
    male = 'men'
    women = 'women'
    gender_CHOICES = (
        (male, 'male'),
        (women, 'women'),
    )
    gender = models.CharField(max_length=100, blank=True, choices=gender_CHOICES)
    releaseDate = models.DateTimeField()
    price = models.IntegerField(null=True)
    get_it_url = models.URLField(null=True)
    description = models.TextField(blank=True, max_length=700)

    def __str__(self):
        return self.brand + " - " + self.title

    @property
    def first_image(self):
        return self.shoeimage_set.first()

    @property
    def date_in_past(self):
        return date.today() > self.releaseDate.date()


class ShoeSpecs(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    spec = models.CharField(max_length=100)


class ShoeImage(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    #  add comments
    #  add gender
    #  add likes
    #  add share URL
    #  add description
    #  add key facts
    #  add countdown timer


