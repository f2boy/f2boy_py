import urllib.request
import urllib.parse
import re
import time
import json
from enum import Enum


class Company(Enum):
    jd = 'jd'
    ali = 'baba'
    momo = 'momo'
    weibo = 'wb'
    snap = 'snap'
    liebao = 'cmcm'
    twitter = 'twtr'
    yy = 'yy'


def getHistory(company):
    print()
    print('开始抓取{}公司数据'.format(company.name))
    url = 'http://www.nasdaq.com/symbol/' + company.value + '/historical'
    req = urllib.request.Request(url)
    req.add_header("Content-Type", "application/json;charset=utf-8")
    response = urllib.request.urlopen(req, ('2y|false|' + company.value.upper()).encode(encoding='UTF8'))
    html = response.read().decode('utf-8')
    html = html.replace('\n', '').replace('\r', '').replace('\t', '').replace('\\', '')

    # html = '<div id="quotes_content_left_pnlAJAX">            <h3 class="table-headtag">                Results for: 5 Days, From 05-JUN-2017  TO 09-JUN-2017             </h3>            <table>                <thead>                    <tr>                        <th>Date</th>                        <th>Open</th>                        <th>                            <a href="javascript:void(0)" class="tt show-link" id="high" onmouseover="showDelayedToolTip(\'high\')" onmouseout="hideToolTip(\'high\')">                                High                                <span class="tooltipLG">                                    <span class="topLG"></span>                                    <span class="middleLG">                                        "High" is the highest sales price the stock has achieved during the regular trading hours, the intra-day high.                                    </span>                                    <span class="bottomLG"></span>                                </span>                            </a>                        </th>                        <th>                            <a href="javascript:void(0)" class="tt show-link" id="low" onmouseover="showDelayedToolTip(\'low\')" onmouseout="hideToolTip(\'low\')">                                Low                                <span class="tooltipLG">                                    <span class="topLG"></span>                                    <span class="middleLG">                                        "Low" is the lowest sales price the stock has fallen to during the regular trading hours, the intra-day low.                                    </span>                                    <span class="bottomLG"></span>                                </span>                            </a>                        </th>                        <th>                            <a href="javascript:void(0)" class="tt show-link" id="close_last" onmouseover="showDelayedToolTip(\'close_last\')" onmouseout="hideToolTip(\'close_last\')">                                Close / Last                                <span class="tooltipLG">                                    <span class="topLG"></span>                                    <span class="middleLG">                                        "Close" is the period at the end of the trading session. Sometimes used to refer to closing price.                                    </span>                                    <span class="bottomLG"></span>                                </span>                            </a>                        </th>                        <th>                            <a href="javascript:void(0)" class="tt show-link" id="volume" onmouseover="showDelayedToolTip(\'volume\')" onmouseout="hideToolTip(\'volume\')">                                Volume                                <span class="tooltipLG">                                    <span class="topLG"></span>                                    <span class="middleLG">                                        "Volume" The closing daily official volumes represented graphically for each trading day.                                    </span>                                    <span class="bottomLG"></span>                                </span>                            </a>                        </th>                    </tr>                </thead>                <tbody>                    <tr>                        <td>                                                    </td>                        <td>                                                    </td>                        <td>                                                    </td>                        <td>                                                    </td>                        <td>                                                    </td>                        <td>                                                    </td>                    </tr>                                                <tr>                                <td>                                    06/09/2017                                </td>                                <td>                                    155.19                                </td>                                <td>                                    155.19                                </td>                                <td>                                    146.02                                </td>                                <td>                                    148.98                                </td>                                <td>                                    64,782,910                                </td>                            </tr>                                                    <tr>                                <td>                                    06/08/2017                                </td>                                <td>                                    155.25                                </td>                                <td>                                    155.54                                </td>                                <td>                                    154.4                                </td>                                <td>                                    154.99                                </td>                                <td>                                    21,144,040                                </td>                            </tr>                                                    <tr>                                <td>                                    06/07/2017                                </td>                                <td>                                    155.02                                </td>                                <td>                                    155.98                                </td>                                <td>                                    154.48                                </td>                                <td>                                    155.37                                </td>                                <td>                                    21,017,560                                </td>                            </tr>                                                    <tr>                                <td>                                    06/06/2017                                </td>                                <td>                                    153.9                                </td>                                <td>                                    155.81                                </td>                                <td>                                    153.78                                </td>                                <td>                                    154.45                                </td>                                <td>                                    26,591,850                                </td>                            </tr>                                                    <tr>                                <td>                                    06/05/2017                                </td>                                <td>                                    154.34                                </td>                                <td>                                    154.45                                </td>                                <td>                                    153.46                                </td>                                <td>                                    153.93                                </td>                                <td>                                    25,277,680                                </td>                            </tr>                                        </tbody>            </table>        </div>'


    content = re.search('<tbody>(.*)</tbody>', html).group(1).replace(' ', '')
    ss = re.findall('<tr><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>',
                    content)

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

    fo = open('/Users/xy/Desktop/stock/' + company.name + '.txt', 'w')
    fo.write(json.dumps(result))
    fo.close()
    print('抓取{}公司数据结束，文件位置：{}'.format(company.name, fo.name))


if __name__ == '__main__':
    for c in Company:
        getHistory(c)
        time.sleep(2)
