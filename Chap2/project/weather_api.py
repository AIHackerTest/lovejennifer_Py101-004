'''
之前只在输入城市名时查询天气，有没有可能指定时间，让程序定时查询天气？
选一个国内 API 进行调用，了解不同的调用姿势。更进一步，如果你来设计 API ，你会怎么设计？
给程序增加温度单位转换功能？
'''
import requests

def fetchWeather(location, unit):
    result = requests.get(
        'https://api.seniverse.com/v3/weather/daily.json',
        params={'key' : 'm8mzdpttjjwj4g5u',
                'location': location,
                'unit': unit},
        timeout=1)
    return result.json()

def words():
    print('''
            输入城市名，返回该城市的天气数据；
            输入h 或 help，打印帮助文档；
            输入quit 或 exit，退出程序；
            输入 c，切换到摄氏度；
            输入 f，切换到华氏度；
            输入 0，查询今天天气；
            输入 1，查询明天天气；
            输入 2，查询后天天气。
            在退出程序之前，会打印查询过的所有城市.
         ''')

def show_weather(result, i, s):
    daily = result['results'][0]['daily'][i]
    date = daily['date']
    name = result['results'][0]['location']['name']
    weather_day = daily['text_day']
    weather_night = daily['text_night']
    temperature_high = daily['high']
    temperature_low = daily['low']
    time = result['results'][0]['last_update'][:-6].replace('T', ' ')
    w = f'{date}, {name}的白天温度为{weather_day}, 夜间温度为{weather_night}, 最高温度为{temperature_high}{s}, 最低温度为{temperature_low}{s}\n更新时间为{time}'
    return w


def search():
    h = []
    unit = 'c'
    i = 0
    s = '摄氏度'
    while True:
        city = input("请输入指令或城市名： ")
        try:
            result = fetchWeather(city, unit)
            w = show_weather(result, i, s)
            print(w)
            h.append(w)
        except KeyError:
            if city in ['h', 'help']:
                words()
            elif city in ['exit', 'quit']:
                break
            elif city in ['0','1','2']:
                i = int(city)
                print('已切换查询日期')
            elif city in ['c','f']:
                unit = city
                s = '华氏度'
                print('已切换温度')
            elif city == 'history':
                for info in h:
                    print(info)
            else:
                print("输入有误，请输入help查询帮助。")


if __name__ == '__main__':
    search()
