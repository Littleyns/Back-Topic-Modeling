from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from pymongo import MongoClient
from . import train
import os
# Create your views here.
def upload(request):
    if request.method == 'POST':
        client =MongoClient('mongodb+srv://root:root@cluster0.yxgu2.mongodb.net/TestDb?retryWrites=true&w=majority')
        study = client.TestDb.stats
        f=request.FILES['myFile']
        with open('train/trainset/'+f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        study.update_one(
            {"field": "studied"},
            {'$inc': {'value': 1}}
        )
        client.close()
    return HttpResponse("success")
def uploadunique(request):
    if request.method == 'POST':
        f = request.FILES['compareto']
        with open('train/compareto/' + f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    return HttpResponse('Success')
def result_show(request):
    if request.method == 'GET':
        filename = os.listdir("train/compareto")[0]
        return JsonResponse(train.train(str(filename)),safe=False)




