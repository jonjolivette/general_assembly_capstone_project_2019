from django.contrib import admin
from .models import Video, Comment, User, Library
# Register your models here.
admin.site.register([Video, Comment, User, Library])
