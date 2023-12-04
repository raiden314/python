import requests
from bs4 import BeautifulSoup

url = "https://www.ymori.com/books/python2nen/test2.html"

html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")
                 #classは予約語だから使えない
chap2 = soup.find(class="chap2")
li = chap2.findAll("li")
for ele in li:
    print(ele.text)