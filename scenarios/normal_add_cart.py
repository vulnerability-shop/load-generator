
import json
import requests
import subprocess
import argparse

def addToCart(auth_token):
    # double check endpoint
    url = "http://127.0.0.1:5182/addToCart?"

    data = {
        "username": username,
        "password": password
        }

    response = requests.post(url, json=data)
    http_status_code = response.status_code

    if http_status_code == 200:
        auth_token = json.loads(response.text)['Token']
        print(auth_token)
    elif http_status_code == 401:
        print(-1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--filePath", type=str, required=False, help="user_migration csv path, if null uses default")

    args = parser.parse_args()

    if args.filePath is not None:
        # Run fetch user for a random username and password with a specified file path
        output = subprocess.check_output(['python', './normal_login.py', '--filePath', str(args.filePath)])
        auth_token = output.decode('utf-8')
    else:
        # Run fetch user for a random username and password
        output = subprocess.check_output(['python', './normal_login.py'])
        auth_token = output.decode('utf-8')

    addToCart(auth_token)


