# DemoDick.py

tp = ("apple", "kiwi")
print( type(tp))
print(len(tp))

# 함수를 정의
def times(a,b):
    return a+b,a*b


print(times(3,4))

args = (5,6)
times(*args)

print("id : %s, name: %s" % ('kim', "김유신"))

# 형식 변환
a = set((1,2))
print(type(a))

b = list(a)
print((b))

b.append(4)
print(b)

colors = {"apple":"red", "kiwi":"green"}
print(len(colors))
print(colors['apple'])


# 장비를 관리한다.
device = {"아이폰": 5, "아이패드":10, "윈도우타블렛":20}
print(len(device))
print(device["아이폰"])

device["맥북"] = 15
device["아이폰"] = 6
del device['아이패드']
print(device)

print(type(False))






#전화번호
phone = {"kim":"1111", "park":"2222"}
for item in phone.items() :
    print(item)

for k,v in phone.items():
    print(k,v)

print("kim" in phone)

print("moon" not in phone)


for key in phone.keys():
    print(key)

for value in phone.values():
    print(value)