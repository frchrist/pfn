from django.contrib import admin
from .models import Course, Level, Subscribe

# Register your models here.

@admin.register(Course)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date", "status")

@admin.register(Level)
class CoureLevelAdmin(admin.ModelAdmin):
    pass

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    pass