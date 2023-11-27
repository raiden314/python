import requests

url = "https://www.ymori.com/books/python2nen/test1.html"

resp = requests.get(url)
resp.encoding = resp.apparent_encoding

filename = "download.txt"
f = open(filename, mode="w", encoding="utf-8")
f.write(resp.text)
f.close()