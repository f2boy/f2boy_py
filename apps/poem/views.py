from django.shortcuts import render


def yzyr(request):
    return render(request, 'poem/yzyr.html')
