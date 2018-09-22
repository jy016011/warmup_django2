import requests
url = "http://10.10.2.155"
souce_code = requests.get(url,allow_redirect=False)
plain_text = source_code.text
print(plain_text)
