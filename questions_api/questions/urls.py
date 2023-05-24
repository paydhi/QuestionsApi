from django.urls import path
from questions.views import QuestionsViewSet

urlpatterns = [
    path('questions/', QuestionsViewSet.as_view()),
]
