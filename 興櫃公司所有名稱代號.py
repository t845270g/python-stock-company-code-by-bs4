a=open('興櫃公司代號.txt','r',encoding="utf-8")
b=a.read()

from bs4 import  BeautifulSoup
soup=BeautifulSoup(b,'html.parser')
l='td'
lm=soup.select(l)
list=[]

for i in range(0,2044,7):
    list.append(lm[i].string.get_text())
print(list)

代號=[]
公司名稱=[]
for i in range(len(list)):
    代號.append(list[i][:4])
    公司名稱.append(list[i][5:])

a.close()

