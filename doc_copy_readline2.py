#정규표현식을 사용
import re 

# 서버의 어디에 로그?
f=open('c:\\work\\PV3.txt','rt')
g=open('c:\\work\\PV3_copy.txt','wt',encoding='utf-8')

#로그 파일이면 100MB ~ 1GB 크기 이상 늘어날 수 있음
#많은 라인의 파일이면 
#한번에 한줄씩 읽어서 처리한다.  
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = f.readline()

# EOF 찾기
while (line != ''):
    # if (re.search("\d{4}", line)):
    if (re.search("error", line)):
        g.write(line + "\n")
    line = f.readline()

f.close() 
g.close()








