from django.urls import path

from . import views
from .views import (
    QuestionApiView,
    QuestionDetailApiView
)

urlpatterns = [
    path('', views.index),
    path('api', QuestionApiView.as_view()),
    path('api/<int:todo_id>/', QuestionDetailApiView.as_view()),
]
