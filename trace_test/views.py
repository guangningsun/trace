# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import json
from models import TraceInfo


def user_login(request):
    pass


def upload_trace(request):
    if request.POST:
        dev1 = TraceInfo(uid=request.POST['uid'],
                         lng=request.POST['lng'],
                         lat=request.POST['lat'],
                         timestamp=request.POST['timestamp']
                         )
        dev1.save()
    return HttpResponseRedirect("/reload_dev_web")


def get_user_list(request):
    pass


def get_trace_list(request):
    list_response = []
    list_dev = TraceInfo.objects.all()
    for res in list_dev:
        dict_tmp = {}
        dict_tmp.update(res.__dict__)
        dict_tmp.pop("_state", None)
        list_response.append(dict_tmp)
    return HttpResponse(json.dumps(list_response), content_type="application/json")


def get_trace_by_uid(request):
    return HttpResponse("<p>删除成功</p>")


def get_all_data(request):
    list_response = []
    list_dev = TraceInfo.objects.all()
    for res in list_dev:
        dict_tmp = {}
        dict_tmp.update(res.__dict__)
        dict_tmp.pop("_state", None)
        list_response.append(dict_tmp)
    return HttpResponse(json.dumps(list_response), content_type="application/json")



