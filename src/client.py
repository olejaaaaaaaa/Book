import requests

CLIENT_ID = '52300662'
REDIRECT_URI = 'https://oauth.vk.com/blank.html'
auth_url = f'https://oauth.vk.com/authorize?client_id={CLIENT_ID}&display=page&redirect_uri={REDIRECT_URI}&scope=friends&response_type=code&v=5.131'
print("Перейдите по следующей ссылке для авторизации:")
print(auth_url)

print("Введите полученный код:")
code = str(input())

# Отправка кода на сервер
auth_code = code
url = 'http://127.0.0.1:5000/auth'
response = requests.post(url, json={'code': auth_code})

if response.status_code == 200:
    print(response.text)
else:
    print(f"Ошибка: {response.text}")