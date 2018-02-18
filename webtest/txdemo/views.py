#  coding=utf-8
from django.shortcuts import render
from txdemo.models import *


def index(request):
    list = BookInfo.objects.all()
    context = {'booklist': list}
    return render(request, 'templates/index2.html', context)


def detail(request, id):
    list = BookInfo.objects.get(id=id).heroinfo_set.all()
    context = {'herolist': list }
    return render(request, 'templates/detail.html', context)


def getform(request):
    # all_messages = UserMessage.objects.all()
    # for message in all_messages:
    # print(message.name)
    if request.method == "POST":
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')
        user_message = UserMessage()
        user_message.name = name
        user_message.message = message
        user_message.address = address
        user_message.email = email
        user_message.object_id = name
        user_message.save()
    return render(request, 'signup.html')
