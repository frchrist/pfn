from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Quize)
class QuizAdmin(admin.ModelAdmin):
    pass


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    pass


@admin.register(Anwser)
class AnwserAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(UserValidQuiz)
class QuizeValidationAdmin(admin.ModelAdmin):
    pass