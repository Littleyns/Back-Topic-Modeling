from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
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
        f=request.FILES['myFile']
        with open('process/Articles/'+f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)


    return HttpResponse("lol")
