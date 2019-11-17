import requests
import json

root_url = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address/'
api_key = ''

# Москва шаболовка
print('Введите адрес для получения подсказок: ')
query = input()

response = requests.post(
    root_url,
    headers={
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Token {api_key}'
    },
    json={ 'query': query }
)

suggestions = json.loads(response.text)['suggestions']

addresses = [suggestion['value'] for suggestion in suggestions]
print(addresses)
