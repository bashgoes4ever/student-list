# coding=utf-8
from django.urls import path
from .views import *


urlpatterns = [
    path('students/', StudentView.as_view()),
    path('marks/', MarksView.as_view()),
]