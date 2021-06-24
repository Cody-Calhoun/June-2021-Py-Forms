from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_user', views.create),
    path('truck_dash', views.dashboard)
]
