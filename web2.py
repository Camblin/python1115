# web2.py

import urllib.request
# 크롤링

from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page={page}"
f =  open("webtool.txt", "a+", encoding="utf-8")
for __page in range(1,6):
    data = urllib.request.urlopen(url.format(page=__page))

    # 검색이 용의한 객체
    soup = BeautifulSoup(data, "html.parser")
    cartoons = soup.find_all("td", class_="title")

    print("갯수{0}".format(len(cartoons)))
    # for cartoon in cartoons :
    #     title = cartoon.find("a").text
    #     link = cartoon.find("a")["href"]
    #     print(title)
    #     print(link)

    for item in cartoons:
        title = item.find("a").text.strip()
        print(title)
        f.write(title + "\n")

f.close()