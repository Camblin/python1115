# DemoForm.py
# DemoForm.ui (UI) + DemoForm.py (로직)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 웹서버에 요청
from bs4 import BeautifulSoup
# 크롤링
import urllib.request

# 화면을 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

# 폼클래스(윈도우)를 정의
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("데모")
    def firstClick(self):
        url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page={page}"
        f =  open("webtool.txt", "wt", encoding="utf-8")
        for __page in range(1,6):
            data = urllib.request.urlopen(url.format(page=__page))
            soup = BeautifulSoup(data, "html.parser")
            cartoons = soup.find_all("td", class_="title")
            print("갯수{0}".format(len(cartoons)))
            for item in cartoons:
                title = item.find("a").text.strip()
                print(title)
                f.write(title + "\n")
        f.close()
        self.label.setText("웹툰 크롤링 종료")
    def secondClick(self):
        self.label.setText("두번째~~")
    def thirdClick(self):
        self.label.setText("세번째~~")

# 진입점을 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()