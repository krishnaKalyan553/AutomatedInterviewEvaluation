from django.shortcuts import redirect, render
from django.http import HttpResponse
from sentence_transformers import SentenceTransformer
import numpy as np
import json 

def home(request):
    return render(request,'home.html')

def test(request):
    questions_list = ["what is your name","how is your day","what are your future plans"]
    rand_questions = {
        "questions_list" : json.dumps(questions_list)  
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



