import json
import requests
import subprocess
import argparse
import random

def purchase(auth_token):
    url = "http://127.0.0.1:5182/addCartItem"

    data = {
        "customer_id": 0,
        "payment_id": 1,
        "Items": 
    }
    # TODO test auth= or this: headers = {'Authorization': auth_token},
    response = requests.post(url, json=data, auth=auth_token)
    http_status_code = response.status_code

    if http_status_code == 200:
        print(f'Added {itemQty} of Item: {itemId} to cart for a random user:')
    elif http_status_code == 401:
        print('Login error in normal add cart')
        exit(1)
    else:
        print('Error in normal add cart')
        exit(1)
    print(f'{nbItems} items added to cart successfully')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--userId", type=int, required=False, help="UserId, if null, will login as random")
    parser.add_argument("--filePath", type=str, required=False, help="user_migration csv path, if null uses default")
    parser.add_argument("--userAuth", type=str, required=False, help="user token, if null will login")
    args = parser.parse_args()

    if args.userAuth is not None:
        auth_token = args.userAuth
    else:
        if args.userId is not None and args.filePath is not None:
            # Run normal login for a defined user id with a specified file path
            output = subprocess.check_output(['python', './normal_login.py', '--userId', str(args.userId),
                                              '--filePath', str(args.filePath)])
        elif args.userId is not None:
            # Run normal login for a defined user id
            output = subprocess.check_output(['python', './normal_login.py', '--userId', str(args.userId)])
        elif args.filePath is not None:
            # Run normal login for a random user id with a specified file path
            output = subprocess.check_output(['python', './normal_login.py', '--filePath', str(args.filePath)])
        else:
            # Run normal login random user id
            output = subprocess.check_output(['python', './normal_login.py'])
        auth_token = output.decode('utf-8')
    output = subprocess.check_output(['python', './normal_add_cart.py', '--userAuth', str(auth_token)])
    purchase(auth_token)


