# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2022-06-08 22:46:20
# @Last Modified by:   Your name
# @Last Modified time: 2022-06-09 00:27:44

from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home),
    
    path('addbook',v.add_book,name='addbook'),
    path('booklist',v.book_list,name='booklist'),
    path('delete/<int:id>',v.delete_book,name="deletebook"),
    path('edit/<int:id>',v.edit_book,name="editbook"),
    
    path('addstd',v.add_std,name='addstd'),
    path('stdlist',v.std_list,name='stdlist'),
    path('delete/<int:id>',v.delete_std,name='deletestd'),
    path('edit/<int:id>',v.edit_std,name='editstd'),
       
    path('login',v.login_view,name='login'),
    path('logout',v.logout_view,name="logout"),
    
    path('about',v.about,name='about'),
]
