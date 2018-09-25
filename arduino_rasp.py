import serial
import urllib.request
serialFromArduino = serial.Serial("/dev/ttyACM0",9600)
serialFromArduino.flushInput()
count = 0 # seat timer
seat_status = False

while True:
    distance = serialFromArduino.readline()
    print(distance)
    if int(distance) <= 70: # if seat is not empty
        if not seat_status:
            seat_status = True
            status = {'num': 1 , 'status': 'seated'}
            data_en =urllib.parse.urlencode(status).encode('utf-8')
            req = urllib.request.Request(url='http://192.168.0.247:8080/show/seat',data = data_en,method='PUT')
            with urllib.request.urlopen(req) as f:
                pass
            print(f.status)
            print(f.reason)
        elif status['status'] == 'empty':
            status = {'num': 1 , 'status': 'seated'}
            data_en =urllib.parse.urlencode(status).encode('utf-8')
            req = urllib.request.Request(url='http://192.168.0.247:8080/show/seat',data = data_en,method='PUT')
            with urllib.request.urlopen(req) as f:
                pass
            print(f.status)
            print(f.reason)
    else:
        count += 1
        print(count)
        if count >= 5:
            seat_status = False
            status = {'num': 1 , 'status': 'empty'}
            data_en =urllib.parse.urlencode(status).encode('utf-8')
            req = urllib.request.Request(url='http://192.168.0.247:8080/show/seat',data = data_en,method='PUT')
            with urllib.request.urlopen(req) as f:
                pass
            print(f.status)
            print(f.reason)
            count = 0