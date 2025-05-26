from django.contrib import admin

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    # for dozen of fild we will split our for to make user friendly
    #None means: no section title.``
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]

admin.site.register(Question, QuestionAdmin)