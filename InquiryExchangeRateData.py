import requests
import urllib
import json

def getData(currencyAmount1=1,currencyName1='美元',currencyName2='人民币'):
    inquiryTextURL = urllib.parse.quote(str(currencyAmount1) + currencyName1 + '等于多少' + currencyName2)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query={0}&co=&resource_id=6017&t=1560408672071&cardId=6017&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json&tn=baidu&cb=jQuery11020513767008117175_1560408665346&_=1560408665348".format(inquiryTextURL)    
    web_data = requests.get(url, headers=header)
    web_data.encoding = 'gbk'
    startPos = web_data.text.index('{')
    endPos = web_data.text.rindex('}') + 1
    datas = json.loads(web_data.text[startPos:endPos])
    result_data = datas['data'][0]
    return result_data

def getCurrency():
    result_data = getData()
    currencyData = []
    for i in range(len(result_data['tab'])):
        for j in range(len(result_data['tab'][i]['moneys']['money'])):
            if result_data['tab'][i]['moneys']['money'][j]['name'] not in currencyData:
                currencyData.append(result_data['tab'][i]['moneys']['money'][j]['name'])
    return currencyData

if __name__ == "__main__": 
    a = getCurrency()
    print(a)