from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Question


class HomeView(LoginRequiredMixin, View):
    template_name = 'questions/home.html'

    def get_context(self):
        asks = Question.objects.all().order_by('-created_at')
        context = {
            'asks': asks,
        }
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context())


class MyProfileView(LoginRequiredMixin, View):
    template_name = 'questions/my_asks.html'

    def get_context(self):
        asks = Question.objects.filter(author=self.request.user).order_by('-created_at')
        context = {
            'asks': asks
        }
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context())


class QuestionDetailView(LoginRequiredMixin, View):
    template_name = 'questions/question_detail.html'
    question_id = None

    def dispatch(self, request, *args, **kwargs):
        self.question_id = kwargs['question_id']
        return super().dispatch(request, *args, **kwargs)

    def get_context(self):
        question = get_object_or_404(Question, pk=self.question_id)
        context = {
            'question': question
        }
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context())

    def post(self, request, *args, **kwargs):
        print(f'El user {request.user} intento enviar algo')