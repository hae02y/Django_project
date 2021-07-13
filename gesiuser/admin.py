from django.contrib import admin
from .models import Gsuser

# Register your models here.

class GsuserAdmin(admin.ModelAdmin):
    list_display = ("username", "useremail", "password")

admin.site.register(Gsuser,GsuserAdmin)