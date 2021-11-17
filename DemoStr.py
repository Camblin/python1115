# DemoStr.py

# print(dir(str))

strA='python is very powerful'
print(len(strA))
print(strA.capitalize())
print(strA.count('p'))
print(strA.count('p', 7))

print('demo.ppt'.endswith("ppt"))
print("MMC2580".isalnum())
print("MMC2580".isdecimal())


# 앞뒤에 공백문자 제거
strB = "<<<  spam and ham  >>>"
print(strB)
print(strB.strip())
result = strB.strip("<> ")
print(result)
#치환하는 경우
result = result.replace('spam', 'spam egg')
lst = result.split()

print(lst)

print("-".join(lst))