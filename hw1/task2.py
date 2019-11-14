import requests
import json

root_url = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address/'
api_key = '715a1d92f578319c5e44be9c2da2e3b72a5ce8f8'

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
