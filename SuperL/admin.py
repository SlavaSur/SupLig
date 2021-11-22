from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Club)
class ClubAdmin (admin.ModelAdmin):
    list_display = ('id','club_name','coutry','rating')