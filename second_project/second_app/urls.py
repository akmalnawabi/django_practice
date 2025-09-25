from django.urls import path
from . import views

urlpatterns = [
  path('function/', views.say_hello),
  path('reservation/', views.home)
]