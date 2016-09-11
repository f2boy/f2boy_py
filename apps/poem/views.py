from django.shortcuts import render


def yzyr(request):
    nav_urls = {}
    nav_urls['sy'] = '上邪'
    nav_urls['yqc'] = '摸鱼儿·雁丘词'
    nav_urls['qjj'] = '将进酒'
    nav_urls['cw'] = '春望'
    nav_urls['waztd'] = '我爱这土地'
    nav_urls['mcdh'] = '面朝大海'
    nav_urls['yzyr'] = '有朝一日'

    return render(request, 'poem/yzyr.html', {'nav_urls': nav_urls})
