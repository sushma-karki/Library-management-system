# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2022-06-08 22:45:13
# @Last Modified by:   Your name
# @Last Modified time: 2022-06-09 01:09:42
from multiprocessing import context
from django.shortcuts import render,redirect,HttpResponse
#from django.http.response import HttpResponse
from .models import book,bookForm
from .models import Std,StdForm
from django.contrib.auth import login,logout,authenticate

from django.contrib.auth.models import User
#from .models import management

def home(request):
    return render(request,"home.html")

def add_book(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        b=book()
        b.name=name
        b.email=email
        b.contact=contact
        b.save()
        return redirect("/")
    else:
        f=bookForm()
        context={'form':f}
        return render(request,"addbook.html",context)
    
def book_list(request):
    blist=book.objects.all()
    context={'blist':blist}
    return render(request,'booklist.html',context)

def delete_book(request,id):
    blist=book.objects.get(id=id)
    blist.delete()
    return redirect('/')

def edit_book(request,id):
    blist=book.objects.get(id=id)
    if request.method=='POST':
        b=bookForm(request.POST,instance=blist)
        if b.is_valid():
            b.save()
            return redirect('/')
        else:
            return render(request,'addbook.html')
    else:
        b=bookForm(instance=blist)
        context={'form':b}
        return render(request,'addbook.html',context)


#--------------------------------------------------------------

def add_std(request):
    if request.method=="POST":
        form=StdForm(request.POST)
        context={'form':form}
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request,"addstd.html",context)
    else:
        form=StdForm()
        context={'form':form}
        return render(request,'addstd.html',context)

def std_list(request):
    slist=Std.objects.all()
    context={'slist':slist}
    return render(request,'stdlist.html',context)


def delete_std(request,id):
    slist=Std.objects.get(id=id)
    slist.delete()
    return redirect('/')
    

def edit_std(request,id):
    slist=Std.objects.get(id=id)
    if request.method=='POST':
        s=StdForm(request.POST,instance=slist)
        s.save()
        return redirect('/')
    else:
        s=StdForm(instance=slist)
        context={'form':s}
        return render(request,'addstd.html',context)


#------------------------------------------------------------------------------------------------   
def login_view(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')

#---------------------------------------------------------------------------------------------------


def about(request):
    return render(request,'about.html')