from django.contrib import admin
from .models import *


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    search_fields = ('title', 'detail')
admin.site.register(Question,QuestionAdmin)
admin.site.register(Comments)
admin.site.register(Vote_up)
admin.site.register(Vote_down)
admin.site.register(Answers)
# Register your models here.
