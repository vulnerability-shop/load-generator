import json
import requests
from modules.fetch_user import fetch_user_credentials


def login_with_credentials(username, password):
    url = 'http://127.0.0.1:5180/login'

    data = {
        'username': username,
        'password': password
    }

    response = requests.post(url, json=data)
    if response.ok:
        auth_token = json.loads(response.text)['token']
        return auth_token
    else:
        return ''


def login_with_id(user_id: int = -1, file_path: str = None):
    username, password = fetch_user_credentials(user_id, file_path)
    return login_with_credentials(username, password)
