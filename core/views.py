from django.shortcuts import render
from django.http import JsonResponse
from .models import PageNumber  # Import the PageNumber model

# Create your views here.

def profile(request):
    return render(request, 'users/profile.html')

def home(request):
    return render(request, 'pages/homepage.html')

def decks(request):
    return render(request, 'pages/decks.html')

def addcard(request):
    return render(request, 'pages/addcard.html')

def randomcardgen(request):
    return render(request, 'pages/randomcardgen.html')

def library(request):
    current_page = 1  # Default to page 1 if no PageNumber object exists
    page_number_object = PageNumber.objects.first()
    if page_number_object:
        current_page = page_number_object.page
    return render(request, 'pages/library.html', {'current_page': current_page})


def update_page_number(request):
    if request.method == 'POST':
        data = request.POST.get('page')
        try:
            page_number = int(data)
            if page_number > 0:
                PageNumber.objects.all().delete()  # Clear existing page number
                PageNumber.objects.create(page=page_number)  # Create new page number
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Invalid page number'})
        except ValueError:
            return JsonResponse({'success': False, 'error': 'Page number must be an integer'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
