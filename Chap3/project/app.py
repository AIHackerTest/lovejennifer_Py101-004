from flask import Flask, request, render_template, url_for
from weather_api import weather

import requests

app = Flask(__name__)
h = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input')
def words():
    try:
        city = request.args.get('city')
        info = weather(city)
        h.append(info)
        return render_template('query.html', info=info)
    except:
        if request.args.get('help') == '帮助':
            return render_template('help.html')
        elif request.args.get('history') == '历史':
            return render_template('history.html', h=h)
        else:
            return render_template('404.html', city=city)


if __name__ == '__main__':
    app.run(debug=True)
