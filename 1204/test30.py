import requests


src = "https://www.ymori.com/books/python2nen/sample1.png"
imgdata = requests.get(src)

filename = "download.png"

with open( filename, mode="wb" ) as f:
    f.write(imgdata.content)