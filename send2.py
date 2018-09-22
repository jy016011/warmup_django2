import urllib.request

if __name__ == "__main__":
    a = urllib.request.Request(url = "http://127.0.0.1",method="GET")
    print(a.data)

