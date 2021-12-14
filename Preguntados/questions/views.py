from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Question, Comment
from .forms import QuestionForm


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


class QuestionCreateView(LoginRequiredMixin, View):
    template_name = 'questions/question_create.html'
    form_class = QuestionForm

    def get_context(self):
        context = {
            'form': self.form_class,
        }
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context())

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
        return redirect(reverse('home-view'))



class QuestionDetailView(LoginRequiredMixin, View):
    template_name = 'questions/question_detail.html'
    question = None

    def dispatch(self, request, *args, **kwargs):
        self.question = get_object_or_404(Question, pk=kwargs['question_id'])
        return super().dispatch(request, *args, **kwargs)

    def get_context(self):
        context = {
            'question': self.question
        }
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context())

    def post(self, request, *args, **kwargs):
        new_comment = request.POST.get('new_comment')
        Comment.objects.create(question=self.question, author=request.user, content=new_comment)
        return self.get(request)