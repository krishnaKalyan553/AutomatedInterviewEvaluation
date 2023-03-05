import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient("mongodb+srv://krishnakalyan:ReryxIGi8VCAtTpB@cluster0.fscwz.mongodb.net/test")
db = client.get_database('Interview_Questions')

dbms = db.dbms

url="https://www.tutorialspoint.com/sql/sql_interview_questions.htm"
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
qsn=soup.find("div",id="mainContent")
lq = qsn.find_all("label")
la=qsn.find_all("div",class_="toggle-content")
# print(len(lq))
# qalist=[]
for i in range(1,len(lq)):
    # l=[]
    if "True or False" not in lq[i].text :
        d = {lq[i].text : la[i].text.replace('\n',"")}
        dbms.insert_one(d)
        # print(d)
    
    
    
    # print(l)

    # dbms.insert()
    # qalist.append(l)
# d = {lq[0].text : la[0].text}
# print(la[0].text)

# for i in qalist:
#     print(i)
#     print()


