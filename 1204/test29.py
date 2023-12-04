import requests
from bs4 import BeautifulSoup

url = "https://news.yahoo.co.jp/categories/it"
html = requests.get(url)

soup = BeautifulSoup(html.content, "html.parser")

#classでフィルターする
div = soup.find(class_="sc-aiIEM")
ul = div.find("ul")
#aというタグを全て取得する 返却はリスト形式
alink = ul.find_all("a")
for ele in alink:
    print(ele.text)