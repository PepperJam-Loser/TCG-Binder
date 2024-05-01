from django.contrib import admin
from core.models import Deck, Card, Collection
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CardResource(resources.ModelResource):
    class Meta:
        model = Card
        fields = ('uuid', 'cardName', 'uri', 'cmc', 'oracle_text', 'img_small', 'img_png')
        import_id_fields = ('uuid',)

class CardAdmin(ImportExportModelAdmin):
    resource_classes = [CardResource]



# Register your models here.
admin.site.register(Deck)
admin.site.register(Collection)

admin.site.register(Card, CardAdmin)
#  admin.site.register(Card) #card is already registered with card admin