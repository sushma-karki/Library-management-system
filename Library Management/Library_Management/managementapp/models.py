# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2022-06-08 22:45:13
# @Last Modified by:   Your name
# @Last Modified time: 2022-06-09 00:15:43
from django.db import models
from django.db.models.base import Model
#from django.http.response import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import datetime as dt 


class book(models.Model):
    name=models.CharField(max_length=30,blank=True)
    email=models.EmailField(max_length=30)
    contact=models.CharField(max_length=30)
    
    class Meta:
        db_table='book'
        
    def __str__(self):
        return self.name


class bookForm(forms.ModelForm):
    class Meta:
        model=book
        fields='__all__' 
    
#----------------------------------------------------------------

class Std(models.Model):
    date=models.DateField()
    name=models.CharField(max_length=15)
    email=models.EmailField(max_length=30)
    bookname=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)

    class Meta:
        db_table='std'

class StdForm(forms.ModelForm):
    class Meta:
        model=Std
        fields='__all__'

    
#-------------------------------------------------------------------
      
class UserInfo(User):
    contact=models.CharField(max_length=15)

    class Meta:
        db_table="userinfo"
    
    
from django import forms
class LoginForm(UserCreationForm):
    class Meta:
        model=UserInfo
        fields=['username','password1','password2']
    
