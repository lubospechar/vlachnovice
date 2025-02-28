from django.contrib import admin
from pivo.models import Brewery, Beer, Tap, Settings


@admin.register(Brewery)
class BreweryAdmin(admin.ModelAdmin):
    pass


@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    pass


@admin.register(Tap)
class TapAdmin(admin.ModelAdmin):
    list_display = ('start', 'beer', 'is_tapped', 'volume', 'price', 'price_per_beer')


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_enabled')


