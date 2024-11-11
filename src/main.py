from flask import Flask, request, jsonify, json
import requests

json.provider.DefaultJSONProvider.ensure_ascii = False
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

CLIENT_ID = '52300662'
CLIENT_SECRET = 'fuE6YqvtM62zAH6V4UpF'
REDIRECT_URI = 'https://oauth.vk.com/blank.html'

@app.get('/')
def all():
    return "{code:'OK'}"

@app.route('/auth', methods=['POST'])
def auth():

    if request.data and request.json:

        token_url = 'https://oauth.vk.com/access_token'

        params = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'redirect_uri': REDIRECT_URI,
            'code': request.json['code']
        }

        response = requests.get(token_url, params=params)
        token_info = response.json()

        if 'access_token' in token_info:
            access_token = token_info['access_token']
            return jsonify({"message": "Аутентификация прошла успешно", "access_token": access_token}), 200
        else:
            return jsonify({"error": "Ошбика Аутентификации"}), 400

    else:
        return jsonify({"error": "Ошибка с запросом или не получен код для аутентификации"})


if __name__ == '__main__':
    app.run(port=5000)  # Запустите локальный сервер