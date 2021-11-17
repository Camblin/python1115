# DemoRE.py
import re
# for item in dir(re):
#     print(item)

result = re.match("[0-9]*th", '35th')

print(result)
print(result.group())

#match와 search 함수의 차이
print( bool(re.match("[0-9]*th", "  35th")))
print( bool(re.search("[0-9]*th", "  35th")))

# 년도 찾기
result = re.search("\d{4}", "올해는 2021년 입니다.")
print( bool(result), result.group())