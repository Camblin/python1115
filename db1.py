# db1.py
import sqlite3

# 연결객체 리턴 받기(임시로 메모리 작업)
# con = sqlite3.connect(":memory:")
con = sqlite3.connect('test.db')

# 실제 구문을 실행한 커서 객체
cur = con.cursor()

from os.path import *
#테이블 구조(스키마)생성
# if not exists('test.db') :
cur.execute("create table PhoneBook(Name text, PhoneNum text);")


# 1건을 입력
cur.execute("insert into PhoneBook values('derick', '010-222');")

#입력 파라메터 처리(입력창을 통해서 받기)
name = "gildong"
phoneNumber = "010-111"
cur.execute("insert into PhoneBook values (?,?);", (name, phoneNumber))

# 다중의 레코드 입력
datalist = (("tom", "010-123"), ("dsp", "010-456"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)


# 데이터 조회
cur.execute("select * from PhoneBook;")
# for row in cur:
#     print(row)
print("--- fetchone()---")
print(cur.fetchone())
print("--- fetchmany()---")
print(cur.fetchmany(2))

print("--- fetchall()---")
cur.execute("select * from PhoneBook;")
for record in cur.fetchall():
    print(record)

print("--- while fetchone()---")
cur.execute("select * from PhoneBook;")
record = cur.fetchone()
while record is not None:
    print(record)
    record = cur.fetchone()


con.commit()
con.close()