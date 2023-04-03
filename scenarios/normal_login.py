import json
import requests
import subprocess
import argparse


def login(username, password):
    url = "http://127.0.0.1:5180/login"

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
    parser.add_argument("--userId", type=int, required=False, help="UserId, if null, will login as random")
    parser.add_argument("--filePath", type=str, required=False, help="user_migration csv path, if null uses default")
    parser.add_argument("--username", type=str, required=False, help="Manual username input")
    parser.add_argument("--password", type=str, required=False, help="Manual password input")
    args = parser.parse_args()

    if args.username is not None and args.password is not None:
        # login with manual username and password
        login(args.username, args.password)
        exit(0)
    elif args.userId is not None and args.filePath is not None:
        # Run fetch user for a defined user id with a specified file path
        output = subprocess.check_output(['python', '../modules/fetch_user.py', '--userId', str(args.userId),
                                          '--filePath', str(args.filePath)])
    elif args.userId is not None:
        # Run fetch user for a defined user id
        output = subprocess.check_output(['python', '../modules/fetch_user.py', '--userId', str(args.userId)])
    elif args.filePath is not None:
        # Run fetch user for a random user id with a specified file path
        output = subprocess.check_output(['python', '../modules/fetch_user.py', '--filePath', str(args.filePath)])
    else:
        # Run fetch user for a random user id
        output = subprocess.check_output(['python', '../modules/fetch_user.py'])

    output_list = output.decode('utf-8').split()
    login(output_list[0], output_list[1])

