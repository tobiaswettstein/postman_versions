from django.shortcuts import render, HttpResponse

import requests
import json
from django.template import RequestContext


def index(request):
    return HttpResponse('Hello World!!!!!!!!<br/><br/> this is my first view')

def show_app_version(request):
    from app.versions import get_app_version, get_canary_version, get_version_info
    return render(request, 'app/versions.html', {'version': get_app_version, 'c_version': get_canary_version, 'info': get_version_info})
