from django.shortcuts import render
from django.http import HttpResponse
from .models import Seats
from django.views.decorators.csrf import csrf_exempt
import urllib.parse as urlparse


@csrf_exempt
def show_seat(request):

	seats = Seats.objects.all()
	str1 = ''
	if request.method == "PUT":
		data_de = request.read().decode('utf-8')
		http_bas = "http://test/test?"
		http_bas += data_de
		parsed = urlparse.urlparse(http_bas)
		seat_num = urlparse.parse_qs(parsed.query)['num'][0]
		seat_status = urlparse.parse_qs(parsed.query)['status'][0]
		print('num',seat_num , 'status',seat_status)
		print(type(seat_num))
		for seat in seats:
			if(seat.seat_num == int(seat_num)):
				seat.is_seat_empty = seat_status
				print(seat.is_seat_empty)
			seat.save()
	context = {'seats' : seats}

	return render(request, 'blog/show_seat.html',context)


# Create your views here.
