from django.http import HttpResponse
from django.shortcuts import render

from apps.message.models import Message


def wall(request):
    message_list = Message.objects.order_by('-id')[:20]
    tem_dict = {}
    for msg in message_list:
        if msg.paper_no not in tem_dict:
            tem_dict[msg.paper_no] = msg

    message_list = []
    for i in range(1, 21):
        if i in tem_dict:
            message_list.append(tem_dict[i])
        else:
            message_list.append(None)

    context = {'message_list': message_list}
    return render(request, 'wall.html', context)


def add(request):
    nickname = request.POST['nickname']
    message = request.POST['message']
    paper_no = request.POST['paper_no']
    q = Message(message_content=message, user_nick=nickname, paper_no=paper_no)
    q.save()

    return HttpResponse("Hello, " + nickname + "！你的留言：" + message)
