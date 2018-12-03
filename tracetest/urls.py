"""tracetest URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from trace_test import views
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tracetest.settings")
django.setup()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user_login/', views.user_login),
    url(r'^upload_trace/', views.upload_trace),
    url(r'^get_user_list/', views.get_user_list),
    url(r'^get_trace_list/', views.get_trace_list),
    url(r'^get_trace_by_uid/', views.get_trace_by_uid),
]
