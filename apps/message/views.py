from django.shortcuts import render


def wall(request):
    return render(request, 'wall.html')
