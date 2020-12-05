from django.contrib import admin

from .models import Chapter, Option, Question, Attempt, User_Answer

# register your models here.
admin.site.register(Chapter)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Attempt)
admin.site.register(User_Answer)
