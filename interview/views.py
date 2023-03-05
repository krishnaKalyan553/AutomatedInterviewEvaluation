from django.shortcuts import redirect, render
from django.http import HttpResponse
from sentence_transformers import SentenceTransformer
import numpy as np
import json 
import pymongo 




def home(request):
    return render(request,'home.html')

def test(request):
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

    rand_questions = {
        "questions_list" : json.dumps(questions_list),

        "answers_list" : json.dumps(answers_list)
        
    }
    return render(request,'test.html',rand_questions)
    


def evaluate(request):
    def eval():
        model = SentenceTransformer('bert-base-nli-mean-tokens')
        original_answer = "Generative Adversarial Networks (GANs) can be described as extremely powerful kinds of neural networks that are employed to aid in Unsupervised Learning. They were created and first introduced in 2014 by Ian J. Goodfellow 2014. GANs are comprised of two neural networks that are in competition with one another and can analyse the changes within a set of data.GANs are a method for generative modelling that uses deep learning methods like CNN (Convolutional Neural Network). Generative modelling is an unsupervised learning method that automatically discovers and learns patterns in input data so that the model can be used for new examples from the original dataset"
        your_answer = "what is a Generative Adversarial Networks"

        text = [original_answer,your_answer]
        sentence_embeddings = model.encode(text)
        similarity_score = np.dot(sentence_embeddings[0], sentence_embeddings[1]) / (np.linalg.norm(sentence_embeddings[0]) * np.linalg.norm(sentence_embeddings[1]))
        print("Cosine similarity score:", similarity_score)

    eval()



