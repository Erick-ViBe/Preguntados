from django.urls import path
from .views import HomeView, MyProfileView, QuestionDetailView, QuestionCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home-view'),
    path('my_asks/', MyProfileView.as_view(), name='my_asks-view'),
    path('new_question/', QuestionCreateView.as_view(), name='question-create'),
    path('question/<int:question_id>/', QuestionDetailView.as_view(), name='question-detail')
]