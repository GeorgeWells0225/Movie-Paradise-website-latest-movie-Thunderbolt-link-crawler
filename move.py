requests  
#from bs4 import BeautifulSoup
import time 
#import pymysql

for n in range(1,50):
    a_url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_'+str(n)+'.html'
    #print(a_url)
    html_1 = requests.get(a_url)
    html_1.encodimport re  
import
ing = 'gb2312'
    #print(html_1.status_code)
    #print(html_1.text)#查看网页源代码
    #re.findall 列表
    detil_list= re.findall('<a href="(.*?)" class="ulink',html_1.text)
    #print(detil_list)
    for m in detil_list:
        b_url = 'http://www.dytt8.net'+m
        #print(b_url)
        html_2 = requests.get(b_url)
        html_2.encoding = 'gb2312'
        #print(html_2.text)
        ftp = re.findall('<a href="(.*?)">.*?</a></td>',html_2.text)
        print(ftp)
        #with open('C:\\Users\\xiang\\Desktop\\666\\dytt.txt','a',encoding='utf-8') as ff:
           #ff.write(ftp[0]+'\n')
