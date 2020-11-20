from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:shoe_id>', views.detail, name='detail'),
]
