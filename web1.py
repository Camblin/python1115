# web1.py

from bs4 import BeautifulSoup

# 페이지를 로딩

page = open(r'c:\work\test01.html', 'rt', encoding="utf-8").read()

# 검색이 용의한 객체 생성
soup = BeautifulSoup(page, "html.parser")

# 전체를 보여달라~
# print(soup.prettify())

# <p> 태그를 몽땅 검색 ==> LIST 형으로 리턴
# for item in soup.find_all("p"):
#     print(">>>>", item)

# 첫번째 <p> 검색
# print(soup.find("p"))

# 필터링 : <p class="outer-text">
# print(soup.find_all("p", class_="outer_text"))

#ID 검색
print(soup.find_all(id="first"))

for tag in soup.find_all("p"):
    # 컨탠츠만 달라 : text 속성
    title = tag.text.strip().replace("\t", "")
    print(title)