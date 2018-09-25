from django.db import models
from django.utils import timezone

class Seats(models.Model):
	is_seat_empty = models.CharField(max_length=200) #seat's status
	seat_num = models.IntegerField(default=0)# seat number

# Create your models here.
