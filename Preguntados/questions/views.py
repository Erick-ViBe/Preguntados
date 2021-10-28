from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin



class HomeView(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        return render(request, 'questions/home.html')