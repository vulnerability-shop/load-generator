import json
import requests
import random
import csv


def fetch_user_credentials(user_id: int = -1):
    users_migration = 'ressources/import_data_Customer.csv'
    with open(users_migration, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        if user_id != -1:
            row = list(csvreader)[user_id]
        else:
            row = random.choice(list(csvreader))
        return row[1], row[2]


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


def login_with_id(user_id: int = -1):
    username, password = fetch_user_credentials(user_id)
    return login_with_credentials(username, password)


def random_login():
    username, password = fetch_user_credentials()
    return login_with_credentials(username, password)
