from django.shortcuts import render

# Create your views here.
# chatbot/views.py

from django.shortcuts import render
import nltk
from nltk.chat.util import Chat, reflections

patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am doing well, thank you!', 'I am fine, how about you?']),
    (r'what is your name', ['My name is ChatBot!', 'I am ChatBot, nice to meet you.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
    # Add more patterns and responses as needed
]

# Create a chatbot instance
chatbot = Chat(patterns, reflections)

def home(request):
    return render(request, 'home.html')

def chat(request):
    return render(request, 'chat.html')
