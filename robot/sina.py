import re
import urllib.request
import json
from enum import Enum


class Attr(Enum):
    name = 1
    cname = 2
    category = 3
    symbol = 4
    price = 5
    diff = 6
    chg = 7
    preclose = 8
    open = 9
    high = 10
    low = 11
    amplitude = 12
    volume = 13
    mktcap = 14
    pe = 15
    market = 16
    category_id = 17


if __name__ == '__main__':
    # url = "http://stock.finance.sina.com.cn/usstock/api/jsonp.php/IO.XSRV2.CallbackList['fa8Vo3U4TzVRdsLs']/US_CategoryService.getList?page=1&num=20&sort=&asc=0&market=&id=";
    # req = urllib.request.Request(url)
    # req.add_header("Content-Type", "application/json; charset=gbk")
    # response = urllib.request.urlopen(req)
    # print(response.read().decode('gbk'))
    # with urllib.request.urlopen(url) as f:
    #     content = f.read().decode('gbk')

    content = 'IO.XSRV2.CallbackList[\'fa8Vo3U4TzVRdsLs\'](({count:"7905",data:[{name:"Apple Inc.",cname:"苹果公司",category:"计算机",symbol:"AAPL",price:"148.98",diff:"-6.01",chg:"-3.88",preclose:"154.99",open:"155.19",high:"155.19",low:"146.02",amplitude:"5.92%",volume:"64882657",mktcap:"782144977570",pe:"17.88475355",market:"NASDAQ",category_id:"5"},{name:"Google Class A shares",cname:"谷歌A类股",category:"媒体内容",symbol:"GOOGL",price:"970.12",diff:"-34.16",chg:"-3.40",preclose:"1004.28",open:"1005.49",high:"1005.50",low:"953.37",amplitude:"5.19%",volume:"3647857",mktcap:"666045583848",pe:"34.79627060",market:"NASDAQ",category_id:"702"},{name:"GOOGLE Inc.",cname:"谷歌",category:"互联网",symbol:"GOOG",price:"949.83",diff:"-33.58",chg:"-3.41",preclose:"983.41",open:"984.50",high:"984.50",low:"935.63",amplitude:"4.97%",volume:"3309389",mktcap:"652115296533",pe:"34.06850953",market:"NASDAQ",category_id:"41"},{name:"CHS Inc - Class B Cumulative Redeemable Preferred Stock, Series ",cname:"CHS Inc - Class B Cumulative Redeemable Preferred Stock, Series ",category:null,symbol:"CHSCL",price:"29.48",diff:"0.21",chg:"0.72",preclose:"29.27",open:"29.10",high:"29.48",low:"29.10",amplitude:"1.30%",volume:"22177",mktcap:"610235990524",pe:null,market:"NASDAQ",category_id:null},{name:"Nuveen High Income November 2021 Target Term Fund Nuveen High In",cname:"Nuveen High Income November 2021 Target Term Fund Nuveen High In",category:null,symbol:"JHB",price:"10.14",diff:"0.00",chg:"0.00",preclose:"10.14",open:"10.13",high:"10.15",low:"10.10",amplitude:"0.49%",volume:"43514",mktcap:"566319019175",pe:null,market:"NYSE",category_id:null},{name:"CHS Inc - Class B Reset Rate Cumulative Redeemable Preferred Sto",cname:"CHS Inc - Class B Reset Rate Cumulative Redeemable Preferred Sto",category:null,symbol:"CHSCM",price:"28.47",diff:"0.01",chg:"0.04",preclose:"28.46",open:"28.55",high:"28.55",low:"28.35",amplitude:"0.70%",volume:"17310",mktcap:"560858986473",pe:null,market:"NASDAQ",category_id:null},{name:"MICROSOFT CP",cname:"微软公司",category:"软件",symbol:"MSFT",price:"70.32",diff:"-1.63",chg:"-2.27",preclose:"71.95",open:"72.03",high:"72.08",low:"68.59",amplitude:"4.85%",volume:"49187396",mktcap:"543573597641",pe:"33.01408259",market:"NASDAQ",category_id:"14"},{name:"HSBC Holdings, plc. Perpetual Sub Cap Secs",cname:"HSBC Holdings, plc. Perpetual Sub Cap Secs",category:null,symbol:"HSEA",price:"27.36",diff:"-0.03",chg:"-0.11",preclose:"27.39",open:"27.40",high:"27.44",low:"27.34",amplitude:"0.37%",volume:"33900",mktcap:"533793611908",pe:"390.85714991",market:"NYSE",category_id:null},{name:"CHS Inc - Class B Cumulative Redeemable Preferred Stock",cname:"CHS Inc - Class B Cumulative Redeemable Preferred Stock",category:null,symbol:"CHSCO",price:"29.29",diff:"0.14",chg:"0.48",preclose:"29.15",open:"29.20",high:"29.34",low:"29.15",amplitude:"0.63%",volume:"13022",mktcap:"529270316544",pe:null,market:"NASDAQ",category_id:null},{name:"CHS INC PFD B SRS 2",cname:"CHS INC PFD B SRS 2",category:null,symbol:"CHSCN",price:"29.66",diff:"0.01",chg:"0.03",preclose:"29.65",open:"29.66",high:"29.66",low:"29.41",amplitude:"0.84%",volume:"10060",mktcap:"498287997437",pe:null,market:"NASDAQ",category_id:null},{name:"Calamos Dynamic Convertible &amp; Income Fund",cname:"Calamos Dynamic Convertible &amp; Income Fund",category:null,symbol:"CCD",price:"20.07",diff:"-0.11",chg:"-0.55",preclose:"20.18",open:"20.33",high:"20.38",low:"19.96",amplitude:"2.08%",volume:"97822",mktcap:"489306592560",pe:null,market:"NASDAQ",category_id:null},{name:"AMAZON.COM INC",cname:"亚马逊公司",category:"互联网",symbol:"AMZN",price:"978.31",diff:"-31.96",chg:"-3.16",preclose:"1010.27",open:"1012.50",high:"1012.99",low:"927.00",amplitude:"8.51%",volume:"7647692",mktcap:"461594049528",pe:"199.65509766",market:"NASDAQ",category_id:"41"},{name:"Facebook Inc.",cname:"Facebook",category:"媒体内容",symbol:"FB",price:"149.60",diff:"-5.11",chg:"-3.30",preclose:"154.71",open:"154.77",high:"155.59",low:"146.61",amplitude:"5.80%",volume:"35577676",mktcap:"427900897458",pe:"42.86533114",market:"NASDAQ",category_id:"702"},{name:"Berkshire Hathaway Inc.",cname:"伯克希尔-哈撒韦B",category:"保险",symbol:"BRK.B",price:"170.00",diff:"3.06",chg:"1.83",preclose:"166.94",open:"167.67",high:"170.14",low:"167.42",amplitude:"1.63%",volume:"3781306",mktcap:"421600000000",pe:"0.01448762",market:"NYSE",category_id:"25"},{name:"Berkshire Hathaway Inc.",cname:"伯克希尔-哈撒韦",category:"保险",symbol:"BRK.A",price:"254965.00",diff:"4660.00",chg:"1.86",preclose:"250305.00",open:"251660.00",high:"255180.00",low:"251280.00",amplitude:"1.56%",volume:"465",mktcap:"418142600000",pe:"21.72844043",market:"NYSE",category_id:"25"},{name:"Johnson & Johnson",cname:"强生公司",category:"制药",symbol:"JNJ",price:"131.53",diff:"0.98",chg:"0.75",preclose:"130.55",open:"130.37",high:"131.70",low:"130.31",amplitude:"1.06%",volume:"5993031",mktcap:"356446296692",pe:"22.18043888",market:"NYSE",category_id:"10"},{name:"Alibaba Group Holding Limited",cname:"阿里巴巴",category:null,symbol:"BABA",price:"139.44",diff:"-2.90",chg:"-2.04",preclose:"142.34",open:"144.57",high:"148.29",low:"137.01",amplitude:"7.92%",volume:"54367382",mktcap:"355014246216",pe:"64.25806338",market:"NYSE",category_id:null},{name:"Exxon Mobil Corporation",cname:"埃克森美孚公司",category:"",symbol:"XOM",price:"82.13",diff:"1.51",chg:"1.87",preclose:"80.62",open:"81.15",high:"82.14",low:"80.69",amplitude:"1.80%",volume:"13553887",mktcap:"340839488602",pe:"43.68616886",market:"NYSE",category_id:"710"},{name:"Fomento Economico Mexicano S.A.B. de C.V. ADS",cname:"Fomento Economico Mexicano S.A.B. de C.V. ADS",category:"饮料",symbol:"FMX",price:"94.89",diff:"-0.66",chg:"-0.69",preclose:"95.55",open:"95.61",high:"95.79",low:"94.50",amplitude:"1.35%",volume:"230230",mktcap:"339706197815",pe:"30.12380842",market:"NYSE",category_id:"74"},{name:"JPMorgan Chase & Co",cname:"摩根大通公司",category:"",symbol:"JPM",price:"86.96",diff:"2.01",chg:"2.37",preclose:"84.95",open:"85.51",high:"87.05",low:"85.39",amplitude:"1.95%",volume:"19120172",mktcap:"310447196732",pe:"14.04846499",market:"NYSE",category_id:"695"}]}));'

    ss = re.search('(.*)\\(\\((.*)\\)\\)', content)
    content = ss.group(2)

    # print(type(content))
    # agent = eval(content, type('Dummy', (dict,), dict(__getitem__=lambda s,n:n))())
    # print(type(agent))
    # print(agent)

    content = content.replace('count:"', '"count":"')
    content = content.replace('data:[', '"data":[')
    content = content.replace('{name:', '{"name":')
    for key in Attr:
        content = content.replace(',' + key.name + ':', ',"' + key.name + '":')

    print(content)

    json_obj = json.loads(content)
    count = json_obj['count']
    data = json_obj['data']
    for key, value in data[0].items():
        print('{} : {}'.format(key, value))

