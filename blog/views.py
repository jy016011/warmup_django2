from django.shortcuts import render
from django.http import HttpResponse
from .models import Seats

def show_seat(request):
	seats = Seats.objects.all()
	str = ''
	for seat in seats:
		str += '{} seat is {}<BR>'.format(seat.seat_num, seat.is_seat_empty)
	return HttpResponse(str) 
# Create your views here.
