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