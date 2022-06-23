from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ThemesForm, TagsForm, QuestionsForm, AnswersForm

def home(request):
    question_list = Question.objects.all()
    themes_list = Theme.objects.all()
    themes_count = themes_list.count()
    question_count = question_list.count()
    tags_count = Tag.objects.all().count()
    context = {'question_list':question_list, 'themes_list':themes_list,'themes_count':themes_count,
    'question_count':question_count,'tags_count':tags_count}
    return render(request, 'questions/dashboard.html', context)

def questions(request):
    questions = Question.objects.all()
    context = {'questions':questions}
    return render(request, 'questions/questions.html', context)

def manage_questions(request,pk=0):
    if pk == 0: #create  
        questions = None                      
    else: #update
        questions = Question.objects.get(id=pk)
    form = QuestionsForm(instance=questions)                         
    if request.method == 'POST':
        form = QuestionsForm(request.POST, instance=questions)
        if form.is_valid():
            form.save()
            return redirect("/questions/")
    context = {'form':form}
    return render(request, 'questions/form.html', context)

def delete_questions(request, pk):
    questions = Question.objects.get(id=pk)
    context = {'item':questions}
    if request.method == 'POST':
        questions.delete()
        return redirect("/questions/")
    return render(request, 'questions/del_questions.html', context)

def themes(request):
    themes = Theme.objects.all()
    context = {'themes':themes}
    return render(request, 'questions/themes.html', context)

# def create_themes(request, pk=0):
#     form = ThemesForm()
#     context = {'form':form}
#     if request.method == 'POST':
#         form = ThemesForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/")
#     return render(request, 'questions/themes_form.html', context)

# def update_themes(request, pk):
#     themes = Theme.objects.get(id=pk)
#     form = ThemesForm(instance=themes)
#     context = {'form':form}
#     if request.method == 'POST':
#         form = ThemesForm(request.POST, instance=themes)
#         if form.is_valid():
#             form.save()
#             return redirect("/themes/")
#     return render(request, 'questions/themes_form.html', context)

def manage_themes(request,pk=0):
    if pk == 0: #create  
        themes = None                      
    else: #update
        themes = Theme.objects.get(id=pk)
    form = ThemesForm(instance=themes)                         
    if request.method == 'POST':
        form = ThemesForm(request.POST, instance=themes)
        if form.is_valid():
            form.save()
            return redirect("/themes/")
    context = {'form':form}
    return render(request, 'questions/form.html', context)


def delete_themes(request, pk):
    themes = Theme.objects.get(id=pk)
    context = {'item':themes}
    if request.method == 'POST':
        themes.delete()
        return redirect("/themes/")
    return render(request, 'questions/del_themes.html', context)

def tags(request):
    tags = Tag.objects.all()
    context = {'tags':tags}

    return render(request, 'questions/tags.html', context)

def manage_tags(request,pk=0):
    if pk == 0: #create  
        tags = None                      
    else: #update
        tags = Tag.objects.get(id=pk)
    form = TagsForm(instance=tags)                         
    if request.method == 'POST':
        form = TagsForm(request.POST, instance=tags)
        if form.is_valid():
            form.save()
            return redirect("/tags/")
    context = {'form':form}
    return render(request, 'questions/form.html', context)


def delete_tags(request, pk):
    tags = Tag.objects.get(id=pk)
    context = {'item':tags}
    if request.method == 'POST':
        tags.delete()
        return redirect("/tags/")
    return render(request, 'questions/del_tags.html', context)

def answers(request, pk):
    questions = Question.objects.get(id=pk)    
    answers  = questions.answer_set.all()
    context = {'questions':questions,'answers':answers}
    return render(request, 'questions/answers.html', context)

def manage_answers(request,pk,sk=0):
    if sk == 0: #create  
        question = Question.objects.get(id=pk)
        answers = Answer(question=question) 
        print("entrou 1")
    else: #update
        answers = Answer.objects.get(id=sk)
        print("entrou 2")
    form = AnswersForm(instance=answers)                         
    if request.method == 'POST':
        form = AnswersForm(request.POST, instance=answers)
        if form.is_valid():
            form.save()
            return redirect("/answers/" + pk)
    context = {'form':form}
    return render(request, 'questions/form.html', context)


def delete_answers(request, pk):
    answers = Answer.objects.get(id=pk)
    context = {'item':answers}
    if request.method == 'POST':
        answers.delete()
        return redirect("/answers/" + str(answers.question.id))
    return render(request, 'questions/del_answers.html', context)    