from django.shortcuts import render
from pivo.models import Tap, Settings
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    try:
        tap = Tap.objects.get(tap=True)
    except Tap.DoesNotExist:
        tap = None


    pub_is_open = Settings.objects.get(pk='open').setting
    self_service = Settings.objects.get(pk='self-service').setting

    if pub_is_open:
        if self_service:
            html_class = 'self-service'
        else:
            html_class = 'open'
    else:
        html_class = 'close'


    return render(request, 'pivo/home.html', {'tap': tap, 'class': html_class })
