from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from sentence_transformers import SentenceTransformer
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import numpy as np
import json 
import pymongo 


answers_list = []
res = {}
def home(request):
    return render(request,'home.html')

def test(request):
    client = pymongo.MongoClient("mongodb+srv://krishnakalyan:ReryxIGi8VCAtTpB@cluster0.fscwz.mongodb.net/test")
    db = client['Interview_Questions']
    col = db['dbms']
    d = list(col.aggregate([ { "$sample": { "size": 2 } } ]))
    questions_list = []
    # global answers_list
    answers_list =  []
    for q_a in d:
        q_a.pop('_id',None)
        questions_list+=(q_a.keys())
        answers_list+=(q_a.values())

    rand_questions = {
        "questions_list" : json.dumps(questions_list),
        "answers_list" : json.dumps(answers_list),
    }
    return render(request,'test.html',rand_questions)
    


def evaluate(request):
    if(request.method =="POST"):
        # data = json.loads(request.body)
        client_ans = json.loads(request.POST["client_ans"])
        our_ans = json.loads(request.POST["our_ans"])
        # global answers_list
        def eval(our_ans,client_ans):
            model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
            res = []
            for i in range(len(our_ans)):  
                print(our_ans[i])
                print(client_ans[i])
                sentence_embeddings = model.encode([our_ans[i],client_ans[i]])
                similarity_score = np.dot(sentence_embeddings[0], sentence_embeddings[1]) / (np.linalg.norm(sentence_embeddings[0]) * np.linalg.norm(sentence_embeddings[1]))
                res.append(max(0,(round(float(similarity_score),4))*100))
                # print("Cosine similarity score:", similarity_score)
            return res
        ress = eval(our_ans,client_ans)
        res = {
            "ress":ress,
        }
        return render(request,"res.html",res)
    else:
        return HttpResponseBadRequest("Answer to check result dont just dive in")