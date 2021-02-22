from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
# Create your views here.
def upload(request):
    if request.method == 'POST':
        f=request.FILES['myFile']
        with open('train/trainset/'+f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)


    return HttpResponse("lol")
