# -*- coding: utf-8 -*-
# @Time     : 2018/4/19 9:43
# @Author   : Narata
# @Project  : demo
# @File     : view.py
# @Software : PyCharm

from django.shortcuts import render
from django.http import HttpResponse


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    callback = request.GET['callback']
    _ = request.GET['_']
    result = "{}({})".format(callback, str({'result': int(a)+int(b)}))
    return HttpResponse(result)