from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from .forms import UploadFileForm

from pymongo import MongoClient
from . import Init

import os
cwd = os.getcwd()
def download(request):
    from django.views.static import serve

    listnames = os.listdir("process/Articles")
    Init.convert(listnames)

    filepath = cwd+'\process\static\Articlestxt.zip'

    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
def upload(request):
    if request.method == 'POST':
        client = MongoClient('mongodb+srv://root:root@cluster0.yxgu2.mongodb.net/TestDb?retryWrites=true&w=majority')
        f=request.FILES['myFile']
        sended = client.TestDb.stats
        with open('process/Articles/'+f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    sended.update_one(
        {"field": "sended"},
        {'$inc': {'value': 1}}
    )
    sended.update_one(
        {"field": "gigabyte"},
        {'$inc': {'value': f.size/(10**9)}}
    )
    client.close()
    return HttpResponse("lol")
