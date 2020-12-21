from django.contrib import admin

# Register your models here.

from .models import Question, choices

admin.site.register(Question)
admin.site.register(choices)
