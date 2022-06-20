from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


def home(request):
    question_list = Question.objects.all()

    context = {'question_list':question_list}
    return render(request, 'questions/dashboard.html', context)

def questions(request):

    pass

