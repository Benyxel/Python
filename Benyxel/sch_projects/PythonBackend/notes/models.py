from django.db import models

# Create your models here.   
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_Name = models.CharField(max_length=255, null=False, blank=False)
    last_Name = models.CharField(max_length=255, null=False, blank=False)
    username =models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    location=models.CharField(max_length=255)
    contact= models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.first_Name} {self.last_Name}'
    
class Note(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Person, on_delete=models.CASCADE, default=1001010)
    title = models.CharField(max_length=255, null=False, blank=False)
    note = models.TextField()
    date= models.DateField(auto_now_add=True) 
    time = models.TimeField(auto_now_add=True)
    status = models.TextField(max_length=255, null=False, blank=False)
    def __str__(self):
        return self.title