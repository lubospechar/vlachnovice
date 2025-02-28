from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from pivo.models import Tap, Settings

class PublicView(View):
    template_name = 'pivo/public.html'

    def get_context_data(self):
        random_image = HomepageImage.get_random_image()
        return {'random_image': random_image}

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)


class HomeView(LoginRequiredMixin, View):
    template_name = 'pivo/home.html'

    def determine_html_class(self, is_pub_open, is_self_service):
        if is_pub_open and is_self_service:
            return 'self-service'
        elif is_pub_open:
            return 'open'
        return 'close'

    def get_context_data(self):
        current_tap = Tap.objects.filter(is_tapped=True).first()
        is_pub_open = Settings.objects.get(pk='open').is_enabled
        is_self_service = Settings.objects.get(pk='self-service').is_enabled

        html_class = self.determine_html_class(is_pub_open, is_self_service)

        return {
            'tap': current_tap,
            'class': html_class
        }

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
