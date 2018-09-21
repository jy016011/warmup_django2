import serial
import urllib.request
serialFromArduino = serial.Serial("/dev/ttyACM0",9600)
serialFromArduino.flushInput()
status = 'empty'
count = 0
seat_num = 1
while True:
    distance = serialFromArduino.readline()
    print(distance)
    if status == 'empty':
        if int(distance) <= 70:
            status = 'seated'
            data_b = (str(seat_num) + "\r\n" + status + "\r\n" + str(distance)).encode('utf-8')
            req = urllib.request.Request(url='192.168.0.180', data= data_b ,method='PUT')
            with urllib.request.urlopen(req) as f:
                print(f.read().decode())
            print(f.status)
            print(f.reason)
        else:
            count += 1
    else:
        if count >= 5:
            status = 'empty'
            data_b = str(seat_num) + "\r\n" + status + "\r\n" + str(distance).encode('utf-8')
            req = urllib.request.Request(url='192.168.0.180', data= data_b ,method='PUT')

            with urllib.request.urlopen(req) as f:
                print(f.read().decode())
            print(f.status)
            print(f.reason)
            count = 0
    
    