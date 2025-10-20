from django.contrib import admin
from .models import Note, Person
# Register your models here.
class NotesCustom(admin.ModelAdmin):
    list_display = ('title' , 'note', 'date', 'time','status')
admin.site.register(Note, NotesCustom)


class PersonView(admin.ModelAdmin):
        list_display = ('first_Name','last_Name','username','email','location','contact','date')
admin.site.register( Person,PersonView)

