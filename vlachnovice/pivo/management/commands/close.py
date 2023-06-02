from django.core.management.base import BaseCommand, CommandError
from pivo.models import Settings

class Command(BaseCommand):
    def handle(self, *args, **options):
        close = Settings.objects.get(pk='open')
        close.setting = False
        close.save()
