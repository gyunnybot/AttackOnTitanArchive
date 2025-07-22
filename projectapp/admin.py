from django.contrib import admin

# Register your models here.
from django.contrib import admin

from articleapp.models import Article
from .models import Project

admin.site.register(Project)
admin.site.register(Article)