from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Prefetch
from .models import PageNumber, Deck, Card, Collection  # Import the PageNumber model
from .forms import DeckForm, CardForm
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView

from django.contrib import messages
from django.db.models import Q

# Create your views here.

def profile(request):
    return render(request, 'users/profile.html')

@login_required
def update_wins_count(request, deck_id):
    if request.method == 'POST' and request.is_ajax():
        deck = Deck.objects.get(id=deck_id)
        if 'increment' in request.POST:
            deck.wins += 1
        elif 'decrement' in request.POST:
            deck.wins -= 1
        deck.save()
        return JsonResponse({'wins': deck.wins})
    else:
        return JsonResponse({'error': 'Invalid request'})




def home(request):
    return render(request, 'pages/homepage.html')

def card_details(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    return render(request, 'pages/card_details.html', {'card': card})

@login_required
def delete_deck(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)
    if request.method == 'POST':
        deck.delete()
    return redirect('decks')


@login_required
def search_cards(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            # Search for cards based on card name or oracle text containing the query
            cards = Card.objects.filter(Q(cardName__icontains=query) | Q(oracle_text__icontains=query))
            card_data = [{'cardName': card.cardName} for card in cards]
            return JsonResponse({'cards': card_data})
        else:
            # If no query provided, return an empty response
            return JsonResponse({'cards': []})



@login_required
def decks(request):
    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid():
            deck_name = form.cleaned_data['deck_name']
            is_public = request.POST.get('is_public') == 'on'
            # Create the new deck with the provided data
            Deck.objects.create(user=request.user, deckName=deck_name, is_public=is_public)
            # Redirect to the decks page after creating the deck
            return redirect('decks')
    else:
        form = DeckForm()

    # Fetch all decks belonging to the logged-in user
    decks = Deck.objects.filter(user=request.user).prefetch_related('cards')

    # Handle search functionality
    if 'q' in request.GET:
        query = request.GET['q']
        # Filter cards based on the search query
        search_results = Card.objects.filter(cardName__icontains=query)
        # Pass the search results and query to the template
        return render(request, 'pages/decks.html', {'decks': decks, 'search_results': search_results, 'query': query, 'form': form})

    # If no search query, render the template with just the decks
    return render(request, 'pages/decks.html', {'decks': decks, 'form': form})



@login_required
def add_card_to_deck(request, card_id):
    if request.method == 'POST':
        card = get_object_or_404(Card, id=card_id)
        deck_id = request.POST.get('deck_id')
        deck = get_object_or_404(Deck, id=deck_id)
        deck.cards.add(card)
    return redirect('decks')


def addcard(request):
    return render(request, 'pages/addcard.html')

def randomcardgen(request):
    return render(request, 'pages/randomcardgen.html')

def library(request):
    if request.method == 'POST':
        return redirect('library')

    # Handle search functionality
    if 'q' in request.GET:
        query = request.GET['q']
        # Filter cards based on the search query
        search_results = Card.objects.filter(cardName__icontains=query)
        # Pass the search results and query to the template
        return render(request, 'pages/library.html', { 'search_results': search_results, 'query': query})

    # If no search query, render the template with just the decks
    return render(request, 'pages/library.html')

def add_card_to_collection(request, card_id):
    if request.method == 'POST':
        card = get_object_or_404(Card, id=card_id)
        
        collection, created = Collection.objects.get_or_create(user=request.user)
        
        collection.cards.add(card)
    return redirect('library')

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
