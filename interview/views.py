from django.shortcuts import  render
from django.http import  HttpResponseBadRequest
from sentence_transformers import SentenceTransformer
import numpy as np
import json
import pymongo 
import random
import os
# import pyrebase

# config = {
#     "apiKey": "AIzaSyCNTJ3TKvM35NvwsrHaIgTeZjtZK9RZKBk", 
#     "authDomain": "automatedinterviewevaluation.firebaseapp.com",
#     "projectId": "automatedinterviewevaluation", 
#     "storageBucket": "automatedinterviewevaluation.appspot.com", 
#     "messagingSenderId": "721658709739", 
#     "appId": "1:721658709739:web:88b0cddb930d4bc54d60ae",
#     "measurementId": "G-K0QT9G77XY",
# }

# firebase  = pyrebase.initialize_app(config)
# storage = firebase.storage()
# storage.child("static/style.css").put("path/to/static/style.css")
# storage.child("static/script.js").put("path/to/static/script.js")
# storage.child("static/images/logo.png").put("path/to/static/images/logo.png")
# functions = firebase.functions()

personality = ["If you could change one thing about your personality, what would it be?",
"Tell me about a stressful scenario in the past and how you handled it.",
"What drives you in your professional life?",
"What makes you unique?",
"what makes you a different engineer",
"What is your greatest fear?",
"What has been the greatest disappointment in your life?",
"Describe a time when you bounced back after a failure.",
"Do you prefer working in a team or on your own? Why?`",]




def home(request):
    return render(request,'home.html')

def test(request):
    load_dotenv()
    security_code = os.getenv('SECURITY_CODE')
    client = pymongo.MongoClient("mongodb+srv://krishnakalyan:"+"1yCYugasJ3sAEjcv@cluster0.fscwz.mongodb.net/test")
    db = client['Interview_Questions']
    col = db['dbms']
    d = list(col.aggregate([ { "$sample": { "size": 2 } } ]))
    questions_list = [random.choice(personality)]
    # questions_list = [personality[5]]
    # global answers_list
    answers_list =  []
    for q_a in d:
        print(q_a)
        q_a.pop('_id',None)
        questions_list+=(q_a.keys())
        answers_list+=(q_a.values())

    # questions_list+=["What is an Entity set?","What is Weak Entity set?","What is kernel?","What is monolithic kernel?"]
    # answers_list+=["The entity set specifies the collection of all entities of a particular entity type in the database. An entity set is known as the set of all the entities which share the same properties.","An entity set that doesnt have sufficient attributes to form a primary key is referred to as a weak entity set. The member of a weak entity set is known as a subordinate entity. Weak entity set does not have a primary key, but we need a mean to differentiate among all those entries in the entity set that depend on one particular strong entity set.","Kernel is the core and most important part of a computer operating system which provides basic services for all parts of the OS.","A monolithic kernel is a kernel which includes all operating system code is in single executable image."]


    rand_questions = {
        "questions_list" : json.dumps(questions_list),
        "answers_list" : json.dumps(answers_list),
    }
    return render(request,'test.html',rand_questions)
    


def evaluate(request):
    if(request.method =="POST"):
        client_ans = json.loads(request.POST["client_ans"])
        our_ans = json.loads(request.POST["our_ans"])
        questions = json.loads(request.POST["ques"])
        def eval(our_ans,client_ans):
            model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
            res = []
            x = len(client_ans)
            y = len(our_ans)
            for i in range(min(x,y)):  
                if(client_ans[i]==""):
                    res.append([questions[i+1]," ",our_ans[i],0])
                    continue
                # print(our_ans[i])
                # print(client_ans[i])
                sentence_embeddings = model.encode([our_ans[i],client_ans[i]])
                similarity_score = np.dot(sentence_embeddings[0], sentence_embeddings[1]) / (np.linalg.norm(sentence_embeddings[0]) * np.linalg.norm(sentence_embeddings[1]))
                res.append([questions[i+1],client_ans[i],our_ans[i],max(0,(round(float(similarity_score),4))*100)])
                # print("Cosine similarity score:", similarity_score)
            return res
        

        ress = eval(our_ans,client_ans)
        res = {
            "ress":ress,
        }
        # print()
        # print(res)
        # print()
        return render(request,"res.html",res)
    else:
        return HttpResponseBadRequest("Answer to check result dont just dive in")
    


def contact(request):
    return render(request,"contact.html")


def about(request):
    return render(request,"about.html")


# functions.deploy()
