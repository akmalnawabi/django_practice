from django.db import models

class MenuItems(models.Model):
  name = models.CharField(max_length=200)
  price = models.IntegerField()
  
class Reservation(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  guest_count = models.IntegerField()
  reservation_time = models.DateField(auto_now=True)
  comments = models.CharField(max_length=200)