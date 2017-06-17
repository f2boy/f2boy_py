#!/usr/local/bin/python3

import json
import os
import re
import time
import urllib.parse
import urllib.request
from enum import Enum

# file_dir = 'd:/'
# file_dir = '/Users/xy/Desktop'
file_dir = '/home/tmp'


class Company(Enum):
    ali = {'code': 'baba', 'name': '阿里巴巴'}
    jd = {'code': 'jd', 'name': '京东'}
    momo = {'code': 'momo', 'name': '陌陌'}
    weibo = {'code': 'wb', 'name': '新浪微博'}
    snap = {'code': 'snap', 'name': 'Snap'}
    liebao = {'code': 'cmcm', 'name': '猎豹移动'}
    twitter = {'code': 'twtr', 'name': '推特'}
    yy = {'code': 'yy', 'name': '歪歪'}
    athm = {'code': 'athm', 'name': '汽车之家'}
    sohu = {'code': 'sohu', 'name': '搜狐'}
    wuba = {'code': 'wuba', 'name': '58同城'}


def format_now():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


def get_history(company):
    print()
    filename = company.name
    code = company.value['code']
    name = company.value['name']
    print(format_now(), '开始抓取【{}】数据'.format(name))
    url = 'http://www.nasdaq.com/symbol/' + code + '/historical'
    req = urllib.request.Request(url)
    req.add_header("Content-Type", "application/json;charset=utf-8")
    response = urllib.request.urlopen(req, ('2y|false|' + code.upper()).encode(encoding='UTF8'), timeout=10)
    html = response.read().decode('utf-8')
    html = html.replace('\n', '').replace('\r', '').replace('\t', '').replace('\\', '')

    content = re.search('<tbody>(.*)</tbody>', html).group(1).replace(' ', '')
    ss = re.findall('<tr><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>', content)

    result = []
    idx = 0
    for s in ss:
        idx += 1

        # 第一行为空的，略过
        if idx == 1:
            continue

        data = []
        t = time.strftime('%Y-%m-%d', time.strptime(s[0], '%m/%d/%Y'))
        data.append(t)
        data.append(s[1])
        data.append(s[4])
        data.append(s[2])
        data.append(s[3])
        # print(data)
        result.append(data)

    fo = open(file_dir + '/stock/' + filename + '.json', 'w')
    fo.write(json.dumps(result))
    fo.close()
    print(format_now(), '抓取【{}】数据结束，文件位置：{}'.format(name, fo.name))


if __name__ == '__main__':
    rs = os.popen('cd ' + file_dir + ';ls stock/').readlines()
    print(format_now(), rs)
    os.popen('cd ' + file_dir + ';rm -rf stock/*')
    os.popen('cd ' + file_dir + ';rm -r stock.zip')

    companies = []
    for c in Company:
        companies.append({'company': c, 'times': 0})

    for ele in companies:
        _c = ele['company']
        try:
            get_history(_c)
        except Exception as e:
            print(format_now(), '抓取【{}】数据异常'.format(_c.value['name']), e)
            times = ele['times']
            if times < 5:
                print(format_now(), '【{}】加入重试队列'.format(_c.value['name']))
                companies.append({'company': _c, 'times': times + 1})
        finally:
            time.sleep(2)

    rs = os.popen('cd ' + file_dir + ';zip -r stock.zip stock').readlines()
    print(format_now(), '压缩抓取数据', rs)
