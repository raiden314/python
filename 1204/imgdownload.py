import requests
from bs4 import BeautifulSoup
import urllib

url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(url)

soup = BeautifulSoup(html.content, "html.parser")

imgele = soup.find_all("img")
for ele in imgele:
    src = ele.get("src")
    imgurl = urllib.parse.urljoin(url,src)
    print(imgurl)
    imgdata = requests.get(imgurl)
    filename = imgurl.split("/")[-1]
    with open( filename, mode="wb" ) as f:
        f.write(imgdata.content)