# DemoError.py

#함수를 정의
def devide(a,b):
    return a/b

# 함수를 호출
try :
    #result = devide(5,0)
    #result = devide(5,"123123")
    result = devide(5,2)
except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")
except TypeError:
    print("숫자여야 합니다.")
else :
    print("결과: {0}".format(result))
finally:
    print("한번 더 체크(무조건 실행)")
print("전체 실행 종료")