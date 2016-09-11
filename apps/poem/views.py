from django.shortcuts import render


def detail(request, curr_poem):
    poems = {}
    poems['sy'] = '上邪'
    poems['yqc'] = '摸鱼儿·雁丘词'
    poems['qjj'] = '将进酒'
    poems['cw'] = '春望'
    poems['waztd'] = '我爱这土地'
    poems['mcdh'] = '面朝大海'
    poems['yzyr'] = '有朝一日'

    if curr_poem not in poems:
        curr_poem = 'yzyr'

    return render(request, 'poem/' + curr_poem + '.html', {'poems': poems, 'curr_poem': curr_poem})
