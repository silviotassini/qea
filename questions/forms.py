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

    def __init__(self, *args, **kwargs):
        super(QuestionsForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['asktext'].widget.attrs['cols'] = 120
        self.fields['asktext'].widget.attrs['rows'] = 10 
        self.fields['asksource'].widget.attrs['size'] = 100   

class AnswersForm(ModelForm):
    class Meta():
        model = Answer
        fields = "__all__" 

    def __init__(self, *args, **kwargs):
        super(AnswersForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['answertext'].widget.attrs['size'] = 120
        