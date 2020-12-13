from django.shortcuts import render, redirect, get_object_or_404
from .models import Shoe
from .models import ShoeImage
from .models import ShoeSpecs
from datetime import datetime
from django.utils import timezone


# Create your views here.


def home(request):
    today = datetime.today()
    shoes_all = Shoe.objects.all()  # <-- All shoes in the database
    image_all = ShoeImage.objects.first()  # <-- All Images in the database
    shoes_not_released = shoes_all.filter(releaseDate__gte=today)  # <-- All shoes filtered by not released
    shoes_release = shoes_all.filter(releaseDate__lte=today)[:5]  # <-- All shoes filtered by release date in the past.
    return render(request, 'shoes/home.html', {'shoes': shoes_all, 'shoes_release': shoes_release,
                                               'shoes_not_released': shoes_not_released,
                                               'image_all': image_all})  # <-- add a new variable.


def detail(request, shoe_id):
    shoe = get_object_or_404(Shoe, pk=shoe_id)
    image_all = ShoeImage.objects.all()
    specs_all = ShoeSpecs.objects.all()

    return render(request, 'shoes/detail.html', {'shoe': shoe, 'image_all': image_all, 'specs_all': specs_all})


def released(request):
    today = datetime.today()
    shoes_all = Shoe.objects.all()  # <-- All shoes in the database
    image_all = ShoeImage.objects.first()  # <-- All Images in the database
    shoes_not_released = shoes_all.filter(releaseDate__gte=today)  # <-- All shoes filtered by not released
    shoes_released = shoes_all.filter(releaseDate__lte=today)  # <-- All shoes filtered by release date in the past.
    return render(request, 'shoes/released.html', {'shoes': shoes_all, 'shoes_released': shoes_released,
                                                   'shoes_not_released': shoes_not_released,
                                                   'image_all': image_all})  # <-- add a new variable.



