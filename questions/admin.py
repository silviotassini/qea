from django.contrib import admin

from .models import *

admin.site.register(Theme)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Note)
admin.site.register(QuestionTag)
admin.site.register(Tag)

