from django.http import HttpResponse
from django.shortcuts import render

from apps.message.models import Message


def wall(request):
    message_list = Message.objects.order_by('-id')[:50]
    context = {'message_list': message_list}
    return render(request, 'wall.html', context)


def add(request):
    nickname = request.POST['nickname']
    message = request.POST['message']
    paper_no = request.POST['paper_no']
    q = Message(message_content=message, user_nick=nickname, paper_no=paper_no)
    q.save()

    return HttpResponse("Hello, " + nickname + "！你的留言：" + message)
