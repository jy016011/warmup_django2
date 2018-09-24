import urllib.request

status = {'num': 2 , 'status': 'seated'}
data_en =urllib.parse.urlencode(status).encode('utf-8')
req = urllib.request.Request(url='http://127.0.0.1:8000/show/seat',data = data_en,method='PUT')
with urllib.request.urlopen(req) as f:
	pass
print(f.status)
print(f.reason)

