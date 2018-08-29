"""Qd_read URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.core.paginator import Paginator
from django.shortcuts import render

import xadmin as admin

from art.models import *

def index(request):
    #查询所有的一级分类
    cates=Category.objects.filter(parent=None)

    #查询所有的文章
    arts=Art.objects.all()
    #获取页码
    page=request.GET.get('page')
    page=int(page) if page else 1
    paginator =Paginator(arts,10) #分页器
    # pager=paginator.page(1)  #读取第一页的数据

    pager=paginator.page(page)


    return render(request,'index.html',locals())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url('', index),
]
