from django.contrib import admin

# Register your models here.
from .models import Artist, Note, Song,Tag


admin.site.register(Artist)
admin.site.register(Song)