from sre_constants import CATEGORY
from sre_parse import CATEGORIES
from telnetlib import STATUS
from django.db import models
from django.template import Origin

# Create your models here.
class Theme(models.Model):    
    theme = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.theme

class Question(models.Model):
    CATEGORY = ((0,'Multiple Choice'),(1,'Right or wrong'))
    theme = models.ForeignKey(Theme, null=True, on_delete=models.SET_NULL)
    asktext = models.CharField(max_length=500, null=False)
    answer_type = models.IntegerField(null=True, choices=CATEGORY)
    asksource = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.asktext

class Answer(models.Model):
    CATEGORY = ((0,'No'),(1,'Yes'))
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
    answertext = models.CharField(max_length=500, null=False)
    iscorrect = models.IntegerField(null=True, choices=CATEGORY)    
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.answertext

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class QuestionTag(models.Model):
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, null=True, on_delete=models.CASCADE)

