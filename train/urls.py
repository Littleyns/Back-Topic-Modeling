from django.urls import path
from . import views
urlpatterns=[
    path('upload/',views.upload,name='train-upload'),
    path('uploadunique/',views.uploadunique,name='train-uploadunique'),
    path('uploadunique/getresult', views.result_show, name='show-result'),
]