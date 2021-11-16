# class1.py
# 클래스를 정의
class Person:
    # 클래스에 소속된 멤버 변수(데이터 공유가 목적)
    num_person = 0
    # 생성자 (초기화 메서드)
    def __init__ (self):
        self.name = "default name"
        Person.num_person += 1
    def print(self):
        print("My name is {0}".format(self.name))
        #print("total person is {}".format(Person.num_person))

#인스턴스 생성
p1 = Person()
p1.name = "전우치"
p2 = Person()
p1.print()
p2.print()
p3 = Person()
print("인스턴스 갯수:{0}".format(Person.num_person))