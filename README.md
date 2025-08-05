# 🌦️ Прогноз погоды, Новости и Цитаты на Flask

Это мини-веб-приложение на Flask, которое отображает:

- Текущий прогноз погоды по введённому городу (OpenWeatherMap)
- Последние новости из России (Лента.ру, RSS)
- Случайную цитату, переведённую на русский язык (API Ninja Quotes)
- Цитата обновляется автоматически каждые 20 секунд с анимацией

---

## 🚀 Как запустить

1. Установи зависимости:

```bash
pip install flask requests googletrans==4.0.0-rc1 python-dotenv
```

2. Создай файл `.env` в корне проекта и вставь туда:

```
OPENWEATHER_API_KEY=твоя_ключ_от_openweathermap
NINJA_QUOTES_API_KEY=твой_ключ_от_api_ninjas
```

3. Запусти приложение:

```bash
python main.py
```

4. Открой в браузере:

```
http://127.0.0.1:5050
```

---

## ⚙️ Структура проекта

```
VD08/
├── main.py
├── .env
└── templates/
    └── index.html
```

---

## 🧠 Используемые технологии

- Flask
- Bootstrap 5
- OpenWeatherMap API (погода)
- RSS лента Лента.ру (новости)
- API Ninja Quotes + Google Translate (цитаты)
- dotenv (для хранения ключей)

---

## 🛡 Безопасность

Все API-ключи хранятся в `.env` и **не публикуются в репозитории**.  
Файл `.env` нужно добавить в `.gitignore`.

---

## 📄 Лицензия

MIT — используй как хочешь 😊

## 👨‍💻 Автор

Сделано [SergeyTatarintcev](https://github.com/SergeyTatarintcev)
