# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json,time
from trace_test.models import TraceInfo, UserInfo


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
        return HttpResponse("{\"error\":0,\"errmsg\":\"upload trace success\"}")
    else:
        return HttpResponse("{\"error\":1,\"errmsg\":\"upload trace false\"}")


def remove_trace_by_id(request):
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
    user_id = request.GET['id']
    if user_id:
        user_info = TraceInfo.objects.get(uid=user_id)
    return HttpResponse(json.dumps(user_info), content_type="application/json")


def create_user(request):
    if request.POST:
        user1 = UserInfo(uid=int(time.time()),
                         username=request.POST['username'],
                         user_role=request.POST['user_role'],
                         password=request.POST['password'],
                         phone_number=request.POST['phone_number']
                         )
        user1.save()
        return HttpResponse("{\"error\":0,\"errmsg\":\"create user success\"}")
    else:
        return HttpResponse("{\"error\":1,\"errmsg\":\"create user false\"}")


def remove_user(request):
    pass


def get_user_by_id(request):
    pass


def get_user_list(request):
    list_response = []
    list_dev = UserInfo.objects.all()
    for res in list_dev:
        dict_tmp = {}
        dict_tmp.update(res.__dict__)
        dict_tmp.pop("_state", None)
        list_response.append(dict_tmp)
    return HttpResponse(json.dumps(list_response), content_type="application/json")


def modify_user_info_by_id(request):
    pass





