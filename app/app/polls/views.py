from datetime import datetime
from django.shortcuts import render
from rest_framework import viewsets

from .models import Poll, Question
from . import serializers


def index(request):
    return render(request, 'index.html')


class PollViewSet(viewsets.ModelViewSet):
    now = datetime.now()
    queryset = Poll.objects.filter(date_start__lt=now, date_end__gt=now)
    serializer_class = serializers.PollSerializer


class QuestioniewSet(viewsets.ModelViewSet):
    now = datetime.now()
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer


