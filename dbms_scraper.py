import requests
from bs4 import BeautifulSoup
url="https://www.tutorialspoint.com/sql/sql_interview_questions.htm"
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
qsn=soup.find("div",id="mainContent")
lq = qsn.find_all("label")
la=qsn.find_all("div",class_="toggle-content")
print(len(lq))
qalist=[]
for i in range(50):
    l=[]
    l.append(lq[i].text)
    l.append(la[i].text)
    qalist.append(l)
for i in qalist:
    print(i)
    print()


