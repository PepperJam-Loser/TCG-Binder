from django.contrib import admin
from django.urls import include, path
from core import views

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
]
