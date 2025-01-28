# Telegram эхо-бот.

## Описание:
Простой Telegram-бота с функционалом “Эхо-бот + Умный фильтр сообщений”

## Функционал:
1. ### Эхо-бот
- Бот отвечает на любое сообщение пользователя отправляя его же текст
2. ### Фильтр сообщений:
- Если сообщение содержит определенные ключевые слова (например, “привет”, “помощь”), 
бот отвечает специальным заранее заданным текстом.
3. ### Хранение статистики сообщений:
- Бот записывает в файл statistics.json информацию о каждом пользователе, который отправил сообщение.
- формат записи:
```json
    "user_id": {
        "username": "имя пользователя",
        "messages_count": "количество сообщений"
    }
```
4. ### Команда /stats:
- По команде /stats бот отправляет пользователю количество сообщений, которые он отправил.
- Если пользователь ещё не отправлял сообщений, бот отправляет: “Вы ещё не отправляли сообщений.”

## Стек технологий:
- Python 3.10
- python-telegram-bot 21.10

## Установка:
1. Клонировать репозиторий:
```commandline
git clone
```
2. Установить зависимости:
```commandline
pip install -r requirements.txt
```
3. Создать файл .env и добавить:
```commandline
BOT_TOKEN = 'ваш токен'
```
4. Запустить bot.py:
```commandline
python bot.py
```



