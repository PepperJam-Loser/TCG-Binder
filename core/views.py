from django.shortcuts import render
# Create your views here.

def profile(request):
    return render(request, 'users/profile.html')

def home(request):
    return render(request, 'pages/homepage.html')

def decks(request):
    return render(request, 'pages/decks.html')

def addcard(request):
    return render(request, 'pages/addcard.html')

def library(request):
    return render(request, 'pages/library.html')