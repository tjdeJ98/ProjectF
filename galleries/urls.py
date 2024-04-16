from django.urls import path
from . import views

urlpatterns = [
    path("", views.galleries, name="galleries"),
    path("plants/", views.plants, name="galleries")
]
