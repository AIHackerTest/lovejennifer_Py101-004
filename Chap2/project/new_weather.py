import requests
import json

KEY = 'm8mzdpttjjwj4g5u'
UID = 'UBD7DA20B2'

LOCATION = 'beijing'
API = 'https://api.seniverse.com/v3/weather/now.json'
UNIT = 'c'
LANGUAGE = 'zh-Hans'


def fetchWeather(location):
    result = requests.get(
        API,
        params={
            'key': KEY,
            'location': location,
            'language': LANGUAGE,
            'unit': UNIT
        },
        timeout=1)
    return result.text

def words():
    print('''
            输入城市名，返回该城市的天气数据；
            输入指令，打印帮助文档（一般使用 h 或 help）；
            输入指令，退出程序的交互（一般使用 quit 或 exit）；
            在退出程序之前，会打印查询过的所有城市.
          ''')

def history(l):
    for i in range(len(l)):
        print(l[i][0], l[i][1], l[i][2] + '摄氏度', l[i][3])

def search():
    h = []
    while True:
        city = input("请输入城市或指令： ")
        try:
            result_json = fetchWeather(city)
            result = json.loads(result_json)
            name = result['results'][0]['location']['name']
            weather = result['results'][0]['now']['text']
            temperature = result['results'][0]['now']['temperature']
            time = result['results'][0]['last_update'][:-6].replace('T', ' ')
            if [city, weather, temperature, time] not in h:
                h.append([city, weather, temperature, time])
                print(f'{name}的天气为{weather},温度为{temperature}摄氏度\n更新时间为{time}')
        except KeyError:
            if city in ['help', 'h']:
                words()
            elif city == 'history':
                history(h)
            elif city in ['exit', 'quit']:
                print('推出前输入历史记录: ')
                history(h)
                break
            else:
                print('输入有误，请输入help查询帮助文档')


search()
