from django.contrib import admin
from .models import ObjectViews


@admin.register(ObjectViews)
class objectAdmin(admin.ModelAdmin):
    list_display = ('content_object', "user", "ip_adress", "timestamp")
# Register your models here.
