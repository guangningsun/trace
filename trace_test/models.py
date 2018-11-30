# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class TraceInfo(models.Model):
    uid = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)
    lat = models.CharField(max_length=20)
    timestamp = models.CharField(max_length=20)


class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user_role = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    uid = models.CharField(max_length=20)