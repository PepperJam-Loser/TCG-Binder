from django.shortcuts import render

# Create your views here.

def profile(request):
    return render(request, 'users/profile.html')

def home(request):
    return render(request, 'pages/homepage.html')