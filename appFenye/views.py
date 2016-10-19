#coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from appFenye import models
import html_helper
#django提供的函数，提供显示标签12345...

# Create your views here.

def test(requst):
    ret = {'data':requst.META.items()}
    return render_to_response('test.html',ret)

def index(request,page):
    #操作数据库进行分页
    # count = models.Host.objects.all()[0:5].count()
    # result = models.Host.objects.all()[0:5]
    per_item = 10
    page =int(page)
    start = (page-1)*per_item
    end = page*per_item
    count = models.Host.objects.all().count()
    result = models.Host.objects.all()[start:end]
    if count%per_item == 0:
        all_pages_count=count/per_item
    else:
        all_pages_count=count/per_item+1
    page=html_helper.Page(page,all_pages_count)
    ret = {'data': result, 'count': count, 'page': page}
    return render_to_response('index.html',ret)
