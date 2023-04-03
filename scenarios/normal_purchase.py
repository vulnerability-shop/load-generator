import json
import requests
import subprocess
import argparse
from modules.add_to_cart import add_to_cart_random
from modules.login import login_with_id

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
    parser.add_argument("--user_id", type=int, required=False, default=-1, help="UserId, if null, will login as random")
    parser.add_argument("--file_path", type=str, required=False, help="user_migration csv path, if null uses default")
    parser.add_argument("--user_auth", type=str, required=False, help="user token, if null will login")
    args = parser.parse_args()

    if args.user_auth is not None:
        auth = args.user_auth
    else:
        auth = login_with_id(args.user_id, args.file_path)
    add_to_cart_random(auth)
    purchase(auth)


