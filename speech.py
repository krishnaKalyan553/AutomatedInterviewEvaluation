import speech_recognition as sr
import pyttsx3
import tensorflow as tf
# import keras
# import tensorflow_hub as hub
import numpy as np
from sentence_transformers import SentenceTransformer

def question(q):
    bot = pyttsx3.init()
    voices = bot.getProperty('voices')
    bot.setProperty('age',20)
    bot.setProperty('rate', 100)
    bot.setProperty('voice', voices[1].id)
    bot.say(q)
    bot.runAndWait()
    bot.stop()
    # if bot._inLoop:
    #     bot.endLoop()
    a = answer()
    return a


def answer():
    recognizer = sr.Recognizer()
    ans = ""
    while True:
        try:
            with sr.Microphone() as mic :
                # recognizer.adjust_for_ambient_noise(mic)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio)
                text = text.lower()
                
                ans+=text

                if 'exit' in text:
                    return ans
                if "don't know" in text:
                    return ""
        except:
            recognizer = sr.Recognizer()
            # print("be a bit louder")
            continue
            # print("something went wrong")
            # break



def eval():
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    original_answer = "Generative Adversarial Networks (GANs) can be described as extremely powerful kinds of neural networks that are employed to aid in Unsupervised Learning. They were created and first introduced in 2014 by Ian J. Goodfellow 2014. GANs are comprised of two neural networks that are in competition with one another and can analyse the changes within a set of data.GANs are a method for generative modelling that uses deep learning methods like CNN (Convolutional Neural Network). Generative modelling is an unsupervised learning method that automatically discovers and learns patterns in input data so that the model can be used for new examples from the original dataset"
    your_answer = question("what is a Generative Adversarial Networks")

    text = [original_answer,your_answer]

    sentence_embeddings = model.encode(text)

    similarity_score = np.dot(sentence_embeddings[0], sentence_embeddings[1]) / (np.linalg.norm(sentence_embeddings[0]) * np.linalg.norm(sentence_embeddings[1]))

    print("Cosine similarity score:", similarity_score)



eval()











# import speech_recognition as sr
# import pyttsx3
# import tensorflow as tf
# import tensorflow_hub as hub
# import numpy as np
# from sentence_transformers import SentenceTransformer

# def home(request):
#     return render(request,'home.html')
# def answer():
#     recognizer = sr.Recognizer()
#     ans = ""
#     while True:
#         try:
#             with sr.Microphone() as mic :
#                 # recognizer.adjust_for_ambient_noise(mic)
#                 audio = recognizer.listen(mic)
#                 text = recognizer.recognize_google(audio)
#                 text = text.lower()
                
#                 ans+=text

#                 if 'exit' in text:
#                     return ans
#                 if "don't know" in text:
#                     return ""
#         except:
#             recognizer = sr.Recognizer()
#             # print("be a bit louder")
#             continue
#         # print("something went wrong")
#         # break
# def question(q):
#     bot = pyttsx3.init()
#     voices = bot.getProperty('voices')
#     bot.setProperty('age',20)
#     bot.setProperty('rate', 100)
#     bot.setProperty('voice', voices[1].id)
#     bot.say(q)
#     bot.runAndWait()
#     bot.stop()
#     # if bot._inLoop:
#     #     bot.endLoop()
#     a = answer()
#     return a

# def eval():
#     model = SentenceTransformer('bert-base-nli-mean-tokens')

#     original_answer = "Generative Adversarial Networks (GANs) can be described as extremely powerful kinds of neural networks that are employed to aid in Unsupervised Learning. They were created and first introduced in 2014 by Ian J. Goodfellow 2014. GANs are comprised of two neural networks that are in competition with one another and can analyse the changes within a set of data.GANs are a method for generative modelling that uses deep learning methods like CNN (Convolutional Neural Network). Generative modelling is an unsupervised learning method that automatically discovers and learns patterns in input data so that the model can be used for new examples from the original dataset"
#     your_answer = question("what is a Generative Adversarial Networks")

#     text = [original_answer,your_answer]

#     sentence_embeddings = model.encode(text)

#     similarity_score = np.dot(sentence_embeddings[0], sentence_embeddings[1]) / (np.linalg.norm(sentence_embeddings[0]) * np.linalg.norm(sentence_embeddings[1]))

#     # print("Cosine similarity score:", similarity_score)
#     # return similarity_score
#     redirect('res.html')

