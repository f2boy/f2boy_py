from django.http import HttpResponse
from django.shortcuts import render


def wall(request):
    return render(request, 'wall.html')


def add(request):
    nickname = request.POST['nickname']
    message = request.POST['message']
    return HttpResponse("Hello, " + nickname + ". 你的留言：" + message)
