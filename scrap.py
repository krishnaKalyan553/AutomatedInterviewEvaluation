# import requests
# from bs4 import BeautifulSoup
# url="https://www.interviewbit.com/dbms-interview-questions/"
# r=requests.get(url)
# soup=BeautifulSoup(r.text,"html.parser")
# qsn=soup.find_all("h3")
# qsn = qsn[2:]
# ans=soup.find_all("article",class_="ibpage-article")
# # print(ans)
# for i in range(len(ans)):
#     # print(qsn[i].text)
#     print(ans[i].text)
#     print("\n\n")
# lq = qsn.find_all("label")
# la=qsn.find_all("div",class_="toggle-content")
# print(len(lq))
# qalist=[]
# for i in range(50):
#     l=[]
#     l.append(lq[i].text)
#     l.append(la[i].text)
#     qalist.append(l)
# for i in qalist:
#     print(i)
#     print()

import pymongo 
import random

client = pymongo.MongoClient("mongodb+srv://krishnakalyan:ReryxIGi8VCAtTpB@cluster0.fscwz.mongodb.net/test")
db = client['Interview_Questions']
col = db['dbms']
d = list(col.aggregate([ { "$sample": { "size": 5 } } ]))
questions_list = []
answers_list =  []
for q_a in d:
    q_a.pop('_id',None)
    questions_list+=(q_a.keys())
    answers_list+=(q_a.values())
