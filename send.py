import requests

if __name__ == "__main__":
    a = requests.get("http://127.0.0.1")
    print(a.text)
