# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2022-06-08 22:44:28
# @Last Modified by:   Your name
# @Last Modified time: 2022-06-08 22:55:07

from django.contrib import admin
from django.urls import path,include
from managementapp.views import home
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('managementapp-',include(('managementapp.urls','managementapp'),namespace='managementapp')),
]