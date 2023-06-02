from django.contrib import admin
from pivo.models import *

@admin.register(Brewery)
class BreweryAdmin(admin.ModelAdmin):
    pass

@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    pass

@admin.register(Tap)
class TapAdmin(admin.ModelAdmin):
    list_display = ('start', 'beer', 'tap', 'volume', 'price', 'price_per_beer')

@admin.register(Settings)
class SetingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'setting')
