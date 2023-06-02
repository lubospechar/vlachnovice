from django.shortcuts import render
from pivo.models import Tap, Settings

def home(request):
    try:
        tap = Tap.objects.get(tap=True)
    except Tap.DoesNotExist:
        tap = None


    pub_is_open = Settings.objects.get(pk='open').setting

    return render(request, 'pivo/home.html', {'tap': tap, 'pub_is_open': pub_is_open})
