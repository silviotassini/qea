from dataclasses import fields
from django.forms import ModelForm
from .models import *

class ThemesForm(ModelForm):
    class Meta():
        model = Theme
        fields = "__all__"

class TagsForm(ModelForm):
    class Meta():
        model = Tag
        fields = "__all__"

class QuestionsForm(ModelForm):
    class Meta():
        model = Question
        fields = "__all__"

class AnswersForm(ModelForm):
    class Meta():
        model = Answer
        fields = "__all__"        