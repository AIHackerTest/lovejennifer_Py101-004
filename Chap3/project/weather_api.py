import requests

def weather(location):
    result = requests.get(
        'https://api.seniverse.com/v3/weather/now.json',
        params={'key' : 'm8mzdpttjjwj4g5u',
                'location': location,
                'unit': 'c'},
        timeout=1)
    result = result.json()
    name = result['results'][0]['location']['name']
    weather = result['results'][0]['now']['text']
    temperature = result['results'][0]['now']['temperature']
    time = result['results'][0]['last_update'][:-6].replace('T', ' ')
    info = [name, weather, temperature, time]
    return info
