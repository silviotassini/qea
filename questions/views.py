from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ThemesForm, TagsForm

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

    return HttpResponse("Pagina questions")

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