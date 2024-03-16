from django.db import models

class PageNumber(models.Model):
    page = models.IntegerField(default=1)  # Default page number is 1

class LastCardIndex(models.Model):
    last_index = models.IntegerField(default=0)

    def __str__(self):
        return f"Last Card Index: {self.last_index}"
