from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv('API_KEY')
city = input('Введите название Вашего города: ').strip()

if not API_KEY:
    print('Нет API_KEY')
    exit()

if city:
    try:
        response = requests.get('https://api.weatherapi.com/v1/current.json', params={'key': API_KEY, 'q': city, 'lang': 'ru'}, timeout=10)
        response.raise_for_status()
        data = response.json()

        name = data['location']['name']
        temp_c = data['current']['temp_c']
        wind_kph = data['current']['wind_kph']
        condition = data['current']['condition']['text']

        print(f'{name} - Температура: {temp_c}°C, скорость ветра: {wind_kph} км/ч, погода: {condition}')
    except requests.exceptions.HTTPError as e:
        error = e.response.json().get('error', {})
        print(f"Ошибка: {error.get('message', 'неизвестная ошибка')}")
    except requests.exceptions.RequestException:
        print('Не удалось получить данные')
    except KeyError as e:
        print(f'В ответе нет такого города или неправильно записано: {e}')
else:
    print('Введите название города!')
