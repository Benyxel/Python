from django.db import models

# Create your models here.
class Note(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    note = models.TextField()
    date= models.DateField(auto_now_add=True) 
    time = models.TimeField(auto_now_add=True)
    status = models.TextField(max_length=255, null=False, blank=False)
    
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_Name = models.CharField(max_length=255)
    last_Name = models.CharField(max_length=255)
    username =models.CharField(max_length=255)
    email = models.EmailField()
    location=models.CharField(max_length=255)
    contact= models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)