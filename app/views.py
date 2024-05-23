from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *

def insert_topic(request):
    TIDO=TopicForm()
    d={'TIDO':TIDO}
    if request.method=='POST':

        TEDO=TopicForm(request.POST)
        if TEDO.is_valid():
            TEDO.save()#automatically save the data

            return HttpResponse('Topic data insert successfully')
        else:
            return HttpResponse('Invalid data')

    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WIDO=WebpageForm()
    d={'WIDO':WIDO}
    if request.method=='POST':

        WEDO=WebpageForm(request.POST)
        if WEDO.is_valid():
            WEDO.save()#automatically save the data

            return HttpResponse('Webpage data insert successfully')
        else:
            return HttpResponse('Invalid data')

    return render(request,'insert_webpage.html',d)

def insert_access(request):
    ARDO=AccessForm()
    d={'ARDO':ARDO}
    if request.method=='POST':

        AEDO=AccessForm(request.POST)
        if AEDO.is_valid():
            AEDO.save()#automatically save the data

            return HttpResponse('Access record data insert successfully')
        else:
            return HttpResponse('Invalid data')

    return render(request,'insert_access.html',d)