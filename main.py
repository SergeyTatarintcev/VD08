from flask import Flask, render_template, request
import requests
import xml.etree.ElementTree as ET
from flask import jsonify
from googletrans import Translator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    city = None

    news = get_news()
    quote, author = get_quote()

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather = get_weather(city)

    return render_template(
        'index.html',
        weather=weather,
        news=news,
        quote=quote,
        author=author
    )


@app.route('/quote')
def get_quote_json():
    quote, author = get_quote()
    return jsonify({'quote': quote, 'author': author})


def get_weather(city):
    api_key = '48f63e1e0bddd12e5b6eaf8a660a9740'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=ru'
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

def get_news():
    url = 'https://lenta.ru/rss/news'
    try:
        response = requests.get(url, timeout=5)
        news_list = []
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            items = root.findall('./channel/item')
            for item in items[:10]:
                title = item.find('title').text
                link = item.find('link').text
                news_list.append({'title': title, 'link': link})
        return news_list
    except Exception as e:
        print("❌ Ошибка загрузки новостей:", e)
        return []

def get_quote():
    api_url = 'https://api.api-ninjas.com/v1/quotes'
    api_key = 'YJ4zrzWxAiYqFsMdtLoUTw==NLM8SCEVGKjcuVIh'

    try:
        response = requests.get(api_url, headers={'X-Api-Key': api_key}, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data:
                quote = data[0]['quote']
                author = data[0]['author']

                # Перевод на русский
                translator = Translator()
                translated_text = translator.translate(quote, dest='ru').text

                return translated_text, author
    except Exception as e:
        print("❌ Ошибка цитаты:", e)

    return "Цитата не найдена", "Неизвестный автор"


if __name__ == '__main__':
    app.run(debug=True, port=5050)
