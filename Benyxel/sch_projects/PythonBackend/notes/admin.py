from django.contrib import admin
from .models import Note
# Register your models here.
class NotesCustom(admin.ModelAdmin):
    list_display = ('title' , 'note', 'date', 'time')
admin.site.register(Note, NotesCustom)