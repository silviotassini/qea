from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


def home(request):
    question_list = Question.objects.all()
    themes_list = Theme.objects.all()
    context = {'question_list':question_list, 'themes_list':themes_list}
    return render(request, 'questions/dashboard.html', context)

def questions(request):

    return HttpResponse("PAgina questions")

def themes(request):
    themes = Theme.objects.all()
    context = {'themes':themes}

    return render(request, 'questions/themes.html', context)

