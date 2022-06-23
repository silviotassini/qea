from django.contrib import admin

from .models import *

admin.site.register(Theme)

admin.site.register(Answer)
admin.site.register(Note)
admin.site.register(QuestionTag)
admin.site.register(Tag)

""" class QuestionAdmin(admin.ModelAdmin):
    fields = ['theme','asktext']
    list_display=['theme','asktext','date_created'] """
admin.site.register(Question)#, QuestionAdmin)