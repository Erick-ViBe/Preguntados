from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ask


class HomeView(LoginRequiredMixin, View):
    template_name = 'questions/home.html'

    def get_context(self):
        asks = Ask.objects.all().order_by('-created_at')
        context = {
            'asks': asks,
        }
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context())


class MyProfileView(LoginRequiredMixin, View):
    template_name = 'questions/my_asks.html'

    def get_context(self):
        asks = Ask.objects.filter(author=self.request.user).order_by('-created_at')
        context = {
            'asks': asks
        }
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context())