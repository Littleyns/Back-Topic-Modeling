from django.urls import path
from . import views
urlpatterns=[
    path('download/',views.download,name='process-download'),
    path('upload/',views.upload,name='process-upload')
]