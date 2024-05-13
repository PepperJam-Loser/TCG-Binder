from django.contrib import admin
from django.urls import include, path
from core import views
from core.views import search_cards, add_card_to_deck, update_wins_count, add_card_to_collection


urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.profile, name="profile"),
    path('decks/', views.decks, name="decks"),
    path('delete_deck/<int:deck_id>/', views.delete_deck, name='delete_deck'),
    path('addcard/', views.addcard, name="addcard"),
    path('library/', views.library, name="library"),
    path('randomcardgen/', views.randomcardgen, name="randomcardgen"),
    path('update_page_number/', views.update_page_number, name="update_page_number"),  # Add this URL pattern
    path('search/', search_cards, name='search_cards'),
    path('add_card_to_deck/<int:card_id>/', views.add_card_to_deck, name='add_card_to_deck'),
    path('add_card_to_collection/<int:card_id>/', views.add_card_to_collection, name='add_card_to_collection'),
    path('card_details/<int:card_id>/', views.card_details, name='card_details'),
    path('update_wins_count/<int:deck_id>/', views.update_wins_count, name='update_wins_count'),
]
