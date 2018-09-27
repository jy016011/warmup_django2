from django.shortcuts import render
from django.http import HttpResponse
from .models import Seats
from django.views.decorators.csrf import csrf_exempt
import urllib.parse as urlparse
#import json


@csrf_exempt
def show_seat(request):

	seats = Seats.objects.all()
	str1 = ''
	if request.method == "PUT": #requet type is PUT
		decoded_data = request.read().decode('utf-8')#decode by UTF-8
		http_bas = "http://django/django?"#to make http form url
		http_bas += decoded_data
		parsed = urlparse.urlparse(http_bas) #parsed from url
		#print(parsed)
		#print(parsed.query)
		seat_num = urlparse.parse_qs(parsed.query)['num'][0]#parsed.query is dict type and seat_num = parsed.query['num'] (key value is 'num')
		seat_status = urlparse.parse_qs(parsed.query)['status'][0]# seat_status = parsed.query['status'] (key value is 'status')
		print('seat num',seat_num , 'seat status',seat_status)
		for seat in seats: # seats objects
			if(seat.seat_num == int(seat_num)): 
				seat.is_seat_empty = seat_status
				print(seat.is_seat_empty)
			seat.save() #commit db changed 
		
	context = {'seats' : seats} #in template 'seats' has seats object's value
	
	return render(request, 'blog/show_seat.html',context) #return response


# Create your views here.
