from django.http import HttpResponse, HttpRequest, JsonResponse
from pymongo import MongoClient
import json
def getstats(request):
    if request.method == 'GET':
        client =MongoClient('mongodb+srv://root:root@cluster0.yxgu2.mongodb.net/TestDb?retryWrites=true&w=majority')
        study = client.TestDb.stats
        stat = {}
        stat['studied']=study.find_one({'field':'studied'})['value']
        stat['sended'] = study.find_one({'field': 'sended'})['value']
        stat['gigabyte'] = study.find_one({'field': 'gigabyte'})['value']
        client.close()
    return JsonResponse(stat)

