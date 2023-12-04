import requests
from bs4 import BeautifulSoup

url = "https://www.ymori.com/books/python2nen/test1.html"
#html構造を取得
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")
# print(soup)

#各タグをタグなしで取得
print( soup.find("title").text )
print( soup.find("h2").text )
print( soup.find("h1").text )

#複数存在するタグを1行ずつ改行して出力する
li = soup.findAll("li")
for ele in li:
    print(ele.text)