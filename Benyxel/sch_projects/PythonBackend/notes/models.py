from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    note = models.TextField()
    date= models.DateField(auto_now_add=True) 
    time = models.TimeField(auto_now_add=True)