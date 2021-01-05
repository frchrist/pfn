from django.contrib import admin
from .models import Course, Level

# Register your models here.

@admin.register(Course)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Level)
class CoureLevelAdmin(admin.ModelAdmin):
    pass