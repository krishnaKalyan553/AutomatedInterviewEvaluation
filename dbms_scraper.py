import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import re
from dotenv import load_dotenv
import os
load_dotenv()

security_code = os.getenv('SECURITY_CODE')
client = MongoClient("mongodb+srv://krishnakalyan:"+security_code)
db = client.get_database('Interview_Questions')

dbms = db.trash

# url="https://www.tutorialspoint.com/sql/sql_interview_questions.htm"
# r=requests.get(url)
# soup=BeautifulSoup(r.text,"html.parser")
# qsn=soup.find("div",id="mainContent")
# lq = qsn.find_all("label")
# la=qsn.find_all("div",class_="toggle-content")
# # print(len(lq))
# # qalist=[]

# q = []
# a = []

# for i in range(0,len(lq)):

#     if "True or False" not in lq[i].text:
#         q.append(lq[i].text)
#         a.append(la[i].text)

# # print(a[-1])

# for i in range(0,len(q)):
#     l = ["/n","/u","/t","/r","/","/n/n",";"]
#     for t in l:
#         q[i] = q[i].replace(t,"").strip()
#         a[i] = a[i].replace(t,"").strip()   

#     q[i] = ' '.join(q[i].strip().split())
#     a[i] = " ".join(a[i].strip().split())
#     # re.sub(r'\n+',' ',q[i]).strip()  
#     # re.sub(r'\n+',' ',a[i]).strip()  
#     d = {q[i] : a[i]}
#     # print(q[i])
#     # print(a[i])
#     # print(d.values())
#     # dbms.insert_one(d)
#     print(d)
#     # print()


    
    
    
#     # print(l)

#     # dbms.insert()
#     # qalist.append(l)
# # d = {lq[0].text : la[0].text}
# # print(la[0].text)

# # for i in qalist:
# #     print(i)
# #     print()



# # s = """

# # hi 

# #  how 

# #  are you

# # """

# # s = s.replace('\n', ' ').strip()
# # print(s)

