# импортируем библиотеку requests

# Пример из библиотеки requests:
    # requests - это библиотека для отправки HTTP-запросов в Python.
    # В этом примере мы отправляем POST-запрос с данными в формате JSON на сервис httpbin.org,
    # который возвращает эти данные обратно, чтобы мы могли увидеть, как это работает.

import requests
import json

    # Данные для отправки

data = {
    'name': 'Hobs',
    'age': 25,
    'country': 'Canada'
}

    # Отправляем POST-запрос на сервер httpbin с данными
response = requests.post('https://httpbin.org/post', json=data)

    # Если запрос успешен (код состояния 200), выводим данные
if response.status_code == 200:
        print("Запрос успешен!")
        # Выводим ответ в формате JSON
        json_data = response.json()  # Преобразуем ответ в формат JSON
        print(json.dumps(json_data, indent=4))  # Преобразуем в красивый формат с отступами
else:
        print("Ошибка запроса! Код состояния:", response.status_code)
