from django.db import models
from django.utils import timezone

class Seats(models.Model):
	is_seat_empty = models.CharField(max_length=200)
	seat_num = models.IntegerField(default=0)
	
# Create your models here.
