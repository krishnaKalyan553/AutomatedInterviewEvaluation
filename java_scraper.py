import requests
from bs4 import BeautifulSoup
url="https://www.tutorialspoint.com/java/java_interview_questions.htm#"
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
#h3,class=h3--> onlt qsns
#qsns=soup.find_all("div",class_="onlycontent")
qsn=soup.find("div",id="mainContent")
#print(qsn)
#ans=soup.find("p")
lq = qsn.find_all("label")
la=qsn.find_all("div",class_="toggle-content")
#print(lq)
#print(len(lq))
#print(lq)
'''d=dict()
for i in range(50):
    d[lq[i]]=la[i]
for i in d:
    print(i.text)
    print(d[i].text)
    print()'''
qalist=[]
for i in range(50):
    l=[]
    l.append(lq[i].text)
    l.append(la[i].text)
    qalist.append(l)
for i in qalist:
    print(i)
    print()









