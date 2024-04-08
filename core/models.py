from django.db import models
from django.contrib.auth.models import User

class PageNumber(models.Model):
    page = models.IntegerField(default=1)  # Default page number is 1

class LastCardIndex(models.Model):
    last_index = models.IntegerField(default=0)

    def __str__(self):
        return f"Last Card Index: {self.last_index}"

class Deck(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    deckName = models.CharField(max_length=50, default='')
    cards = models.ManyToManyField('Card')

    def __str__(self):
        return f"{self.deckName} - Deck for {self.user.username}"

class Card(models.Model):
    cardName= models.CharField(max_length=50)

    def __str__(self):
        return f"Card {self.cardName}"

