# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.

import random
import matplotlib.pyplot as plt
import requests
import json

# Прогноз погоды
#def weather_answer(city):
city='Novosibirsk'
url = ('https://api.weather.yandex.ru/v2/forecast' )


# Задаем координаты населенного пункта
lat = 55.75396 # широта Москвы
lon = 37.620393 # долгота Москвы

# Задаем параметры запроса
params = {
    'lat': lat,
    'lon': lon,
    'lang': 'ru_RU', # язык ответа
    'limit': 7, # срок прогноза в днях
    'hours': True, # наличие почасового прогноза
    'extra': False # подробный прогноз осадков
}

# Задаем значение ключа API
api_key = '041533d7-d5c5-42ab-aca2-6627db4b69d3'

# Задаем URL API
url = 'https://api.weather.yandex.ru/v2/forecast'

# Делаем запрос к API
response = requests.get(url, params=params, headers={'X-Yandex-API-Key': api_key})
print(response)
'''weather_data = requests.get(url).json()
weather_data_structure = json.dumps(weather_data, indent=2)
'''
'''temperature = weather_data['main']['temp']
feels_like = weather_data['main']['feels_like']
wind = weather_data['wind']['speed']'''

    #return f'Температура {round(temperature)} градусов, ощущаеться как {round(feels_like)} градусов. Скорость ветра {wind} м/с'



'''

temp=[random.randint(-10, 36) for i in range(365)]
average_temp=sum(temp)/365
higher_25=0
max_len = 0
line = 1
for i in range(365):
    if temp[i]>25:
        higher_25+=1

    if temp[i] < 0:
        line += 1
    else:
        if line > max_len:
            max_len = line
        line = 1
print('Подряд ниже 0:', max_len)
print('Выше 25:', higher_25)

plt.plot(temp, color='blue')
plt.title("Погода")
plt.show()
'''