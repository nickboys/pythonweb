# -*- coding: utf-8 -*-

from django.http import HttpResponse

from myApp.models import App

# 数据库操作
def testdb(request):
    test1 = App(name='huangjian')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")