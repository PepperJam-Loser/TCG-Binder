from django import forms

class DeckForm(forms.Form):
    deck_name = forms.CharField(max_length=50)

class CardForm(forms.Form):
    card_name = forms.CharField(max_length=50)
    deck_nameCard = forms.CharField(max_length=50)