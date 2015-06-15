from django import forms
from django.db import models

class Attachment(models.Model):
    file = models.FileField(upload_to='documents/%Y/%m/%d', blank=True, null= True)

# Create your models here.
class User(models.Model):
    account = models.CharField(max_length = 45, unique = True)
    password = models.CharField(max_length = 45)
    type = models.CharField(max_length = 10)
    
    def __unicode__(self):
        return self.type + "_" + self.account

class Alumni(models.Model):
    user = models.ForeignKey(User)
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.EmailField(max_length = 45,unique=True)
    graduate_date = models.DateField()
    gender = models.CharField(max_length = 45)
    picture = models.ImageField(upload_to = "images/", blank =True, null = True)
    status = models.CharField(max_length = 10)
    
    def __unicode__(self):
        return self.first_name + " " + self.last_name
    
class Education_Exp(models.Model):
    alumni = models.ForeignKey(Alumni)
    major = models.CharField(max_length = 45)
    start_date = models.DateField()
    end_date = models.DateField()
    school = models.CharField(max_length = 45)
    address = models.CharField(max_length = 45)   
    city = models.CharField(max_length = 45)
    state = models.CharField(max_length = 45)
    zip = models.CharField(max_length = 45)
    description = models.TextField(max_length = 400)
    
    def __unicode__(self):
        return self.alumni.first_name + " " + self.alumni.last_name + "_" + self.school
    
class Working_Exp(models.Model):
    alumni = models.ForeignKey(Alumni)
    title = models.CharField(max_length = 45)
    start_date = models.DateField()
    end_date = models.DateField()
    company = models.CharField(max_length = 45)
    address = models.CharField(max_length = 45)
    city = models.CharField(max_length = 45)
    state = models.CharField(max_length = 45)
    zip = models.CharField(max_length = 45)
    description = models.TextField()
    
    def __unicode__(self):
        return self.alumni.first_name + " " + self.alumni.last_name + "_" + self.company
    
class Group(models.Model):
    name = models.CharField(max_length = 45, unique = True)
    alumnis = models.ManyToManyField(Alumni)
    
    def __unicode__(self):
        return self.name
    
class Message(models.Model):
    subject = models.CharField(max_length = 45, unique = True)
    date = models.DateTimeField()
    abstract = models.TextField()
    docfile = models.FileField(upload_to='documents/%Y/%m/%d', blank=True, null= True)
    def __unicode__(self):
        return self.subject


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        required = False,
        label='Select .pdf file',
        help_text='max. 42 megabytes'
    )