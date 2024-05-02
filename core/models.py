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
        return f"{self.deckName} by {self.user.username}"

class Card(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=100, default='')
    cardName = models.CharField(max_length=100, default='')
    uri = models.CharField(max_length=256, default='')
    cmc = models.IntegerField(default=0)
    oracle_text = models.CharField(max_length=256, default='')
    img_small = models.CharField(max_length=256, default='')
    img_png = models.CharField(max_length=256, default='')

    def __str__(self):
        return f"{self.cardName}"

class Collection(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    cards = models.ManyToManyField('Card')

    def __str__(self):
        return f"{self.user.username}'s Collection"


