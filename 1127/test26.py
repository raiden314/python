import requests

url = "https://www.ymori.com/books/python2nen/test1.html"

resp = requests.get(url)
resp.encoding = resp.apparent_encoding

print(resp.text)