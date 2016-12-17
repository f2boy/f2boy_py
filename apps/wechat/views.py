from django.http import HttpResponse


def verify(request):
    signature = request.GET["signature"]
    timestamp = request.GET["timestamp"]
    nonce = request.GET["nonce"]

    echostr = request.GET["echostr"]
    print(echostr)
    return HttpResponse(echostr)
