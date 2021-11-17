#DemoOS.py
import random

print(random.random())
print(random.random())
print([random.randrange(0,20) for i in range(10)])
print(random.sample(range(20),5))

# 파일 이름 다루기
from os.path import *
print(abspath("python.exe"))
print(basename("C:\\work\\python.exe"))
print(getsize("C:\\python38\\python.exe"))
print("normpath : ", normpath(r"C:/ython38/python.exe"))

import os
print("운영체제 이름:", os.name)
# os.system("notepad.exe")

# 파일 리스트, 폴더 리스트
import glob
for file in glob.glob(r'C:\work\*.py'):
    print(file)

os.chdir("../")
print("현재 작업 폴더", os.getcwd())
os.chdir(r"C:\work")
for item in glob.glob("*"):
    print("- ",  "isfile(", str(isfile(item)).rjust(5) , ")", item)