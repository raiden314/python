import requests
from bs4 import BeautifulSoup

url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(url)

soup = BeautifulSoup(html.content, "html.parser")

imgele = soup.find_all("img")
for ele in imgele:
    src = ele.get("src")
    print(src)