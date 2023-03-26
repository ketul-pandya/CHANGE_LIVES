from django.db import models

# Create your models here.
from django.db.models import Model

class Signup(models.Model):
    user=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    
    def __str__(self):
        return self.user
    
# class Contact(models.Model):
    
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=50)
    ph_no=models.CharField(max_length=13)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class Registration(models.Model):
    name=models.CharField(max_length=125)
    registration_no=models.IntegerField()
    phone_no=models.IntegerField(max_length=10)
    state=models.CharField(max_length=50)
    document=models.FileField(upload_to='pdfs/')
    email=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    author_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    