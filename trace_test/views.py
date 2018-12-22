# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json,time
from trace_test.models import TraceInfo, UserInfo


def user_login(request):
    pass

# success 
def upload_trace(request):
    #import pdb;pdb.set_trace()
    current_time = time.time()
    if request.POST:
        dev1 = TraceInfo(uid=request.POST.get('uid'),
                         lng=request.POST.get('lng'),
                         lat=request.POST.get('lat'),
                         timestamp=current_time
                         )
        dev1.save()
        return HttpResponse("{\"error\":0,\"errmsg\":\"upload trace success\"}",content_type="application/json")
    else:
        return HttpResponse("{\"error\":1,\"errmsg\":\"upload trace false\"}",content_type="application/json")


def remove_trace_by_id(request):
    pass


# success 
def get_trace_list(request):
    list_response = []
    list_dev = TraceInfo.objects.all()
    for res in list_dev:
        dict_tmp = {}
        dict_tmp.update(res.__dict__)
        dict_tmp.pop("_state", None)
        list_response.append(dict_tmp)
    return HttpResponse(json.dumps(list_response), content_type="application/json")

# success 
def get_trace_by_uid(request):
    if request.POST:
        user_id = request.POST['user_id']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        if user_id:
            list_response = []
            list_dev = TraceInfo.objects.filter(uid=user_id).filter(timestamp__gt=start_time).filter(timestamp__lt=end_time)
            for res in list_dev:
                dict_tmp = {}
                dict_tmp.update(res.__dict__)
                dict_tmp.pop("_state", None)
                list_response.append(dict_tmp)
            return HttpResponse(json.dumps(list_response), content_type="application/json")
        else:
            return HttpResponse("{\"error\":1,\"errmsg\":\"the trace info that you request doesn`t exist\"}")
    else: 
        return HttpResponse("{\"error\":1,\"errmsg\":\"the trace info that you request doesn`t exist\"}")


# success
def get_trace_by_traceid(request):
    if request.POST:
        trace_id = request.POST['trace_id']
        if trace_id:
            trace_info = {}
            trace_info.update(TraceInfo.objects.get(id=trace_id).__dict__)
            trace_info.pop("_state", None)
            return HttpResponse(json.dumps(trace_info), content_type="application/json")
        else:
            return HttpResponse("{\"error\":1,\"errmsg\":\"the trace info that you request doesn`t exist\"}")
    else:
        return HttpResponse("{\"error\":1,\"errmsg\":\"the trace info that you request doesn`t exist\"}")

# success
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


# success 
def get_user_by_uid(request):
    if request.POST:
        user_id = request.POST['user_id']
        if user_id:
            user_info = {}
            user_info.update(UserInfo.objects.get(uid=user_id).__dict__)
            user_info.pop("_state", None)
        return HttpResponse(json.dumps(user_info), content_type="application/json")
    else: 
        return HttpResponse("{\"error\":1,\"errmsg\":\"the user that you request doesn`t exist\"}")


# success 
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


def obj_2_json(obj):
    return {}


