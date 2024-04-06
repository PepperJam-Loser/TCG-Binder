from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Prefetch
from .models import PageNumber, Deck, Card  # Import the PageNumber model
from .forms import DeckForm, CardForm

# Create your views here.

def profile(request):
    return render(request, 'users/profile.html')

def home(request):
    return render(request, 'pages/homepage.html')

@login_required
def decks(request):
    if request.method == 'POST':
        deckFormIN = DeckForm(request.POST)
        cardFormIN = CardForm(request.POST)
        if deckFormIN.is_valid():
            deck_name = deckFormIN.cleaned_data['deck_name']
            user = request.user
            deck = Deck.objects.create(user=user, deckName=deck_name)
            return redirect('decks')  # Redirect to the same page after adding the deck
        if cardFormIN.is_valid():
            card_name = cardFormIN.cleaned_data['card_name']
            deck_nameCard = cardFormIN.cleaned_data['deck_nameCard']
            # Check if the card already exists in the database
            existing_card = Card.objects.filter(cardName=card_name).first()
            existing_deck = Deck.objects.get(deckName=deck_nameCard)
            if existing_card:
                pass
            else:
                existing_card = Card.objects.create(cardName=card_name)
            existing_deck.cards.add(existing_card)
            return redirect('decks')  # Redirect to the same page after adding the deck
    else:
        deckFormIN = DeckForm()
        cardFormIN = CardForm()
    decks = Deck.objects.filter(user=request.user).prefetch_related('cards')
    return render(request, 'pages/decks.html', {'form': deckFormIN, 'form':cardFormIN, 'decks': decks})

@login_required
def delete_deck(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)
    if request.method == 'POST':
        deck.delete()
    return redirect('decks')

@login_required
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
