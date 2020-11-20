from django.shortcuts import render, redirect, get_object_or_404
from .models import Shoe

# Create your views here.


def home(request):
    shoes = Shoe.objects.all()
    return render(request, 'shoes/home.html', {'shoes': shoes})


def detail(request, shoe_id):
    shoe = get_object_or_404(Shoe, pk=shoe_id)
    return render(request, 'shoes/detail.html', {'shoe': shoe})
