from django.contrib import admin
from .models import *
# Register your models here.

class listClass(admin.ModelAdmin):
    list = "fname", "lname", "username", "email", "password", "profilePic"

class postList(admin.ModelAdmin):
    list = "title", "description", "time"
admin.site.register(profileInformations, listClass)
admin.site.register(userPost, postList)