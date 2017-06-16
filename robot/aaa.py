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
    ali = 'baba'
    jd = 'jd'
    momo = 'momo'
    weibo = 'wb'
    snap = 'snap'
    liebao = 'cmcm'
    twitter = 'twtr'
    yy = 'yy'
    athm = 'athm'
    sohu = 'sohu'
    wuba = 'wuba'


def get_history(company):
    print()
    print('开始抓取{}公司数据'.format(company.name))
    url = 'http://www.nasdaq.com/symbol/' + company.value + '/historical'
    req = urllib.request.Request(url)
    req.add_header("Content-Type", "application/json;charset=utf-8")
    response = urllib.request.urlopen(req, ('2y|false|' + company.value.upper()).encode(encoding='UTF8'))
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
        print(data)
        result.append(data)

    fo = open(file_dir + '/stock/' + company.name + '.json', 'w')
    fo.write(json.dumps(result))
    fo.close()
    print('抓取{}公司数据结束，文件位置：{}'.format(company.name, fo.name))


if __name__ == '__main__':
    # ll = []
    # for c in Company:
    #     ll.append(c)
    # 
    # for l in ll:
    #     print(l)
    #     if l.name == 'ali':
    #         ll.append(Company.twitter)
    #     if l.name == 'jd':
    #         ll.append(Company.ali)

    s = os.popen('cd ' + file_dir + ';ls stock/').readlines()
    print(s)
    s = os.popen('cd ' + file_dir + ';rm -rf stock/*').readlines()
    print(s)
    s = os.popen('cd ' + file_dir + ';rm -r stock.zip').readlines()
    print(s)

    for c in Company:
        get_history(c)
        time.sleep(2)
        # todo 超时重试

    s = os.popen('cd ' + file_dir + ';zip -r stock.zip stock').readlines()
    print(s)
