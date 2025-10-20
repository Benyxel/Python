from django.contrib import admin
from .models import Note
# Register your models here.
class NotesCustom(admin.ModelAdmin):
    list_display = ('id', 'title' , 'note', 'date', 'time','status')
admin.site.register(Note, NotesCustom)