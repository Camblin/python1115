# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}
addr = 'http://www.todayhumor.co.kr'
for n in range(1,11):
        #클리앙의 중고장터 주소 
        data = addr + '/board/list.php?table=bestofbest&page=' + str(n)
        # print(">> URL : {}".format(data))
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class': "subject"})

# <tr class="view list_tr_sisa" mn="481523">
# 			<td class="subject"><a href="/board/view.php?table=bestofbest&amp;no=447637&amp;s_no=447637&amp;page=1" target="_top">오징어게임 감독도 이명박근혜의 블랙리스트</a><span class="list_memo_count_span"> [16]</span>  <span style="margin-left:4px;"><img src="http://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> </span> </td>
# 		</tr>

        for item in list:
                try:
                        a = item.find("a")
                        title = a.text.strip()
                        # print(title)
                        if (re.search('오징어게임', title)):
                                 print(" 제목 : {} ({})".format(title, addr + a['href']))
                                #  print(addr  + item['href'])
                except:
                        pass
        
