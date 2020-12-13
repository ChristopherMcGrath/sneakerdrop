from django.urls import path

from . import views

urlpatterns = [
    path('<int:shoe_id>', views.detail, name='detail'),
    path('', views.released, name='released'),
]
