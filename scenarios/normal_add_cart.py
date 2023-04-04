import requests
import subprocess
import argparse
import random
from modules.login import login_with_id
from modules.add_to_cart import add_to_cart_random


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--user_id', type=int, required=False, default=-1, help='user_id, if null, will login as random')
    parser.add_argument('--file_path', type=str, required=False, help='user_migration csv path, if null uses default')
    parser.add_argument('--user_auth', type=str, required=False, help='user token, if null will login')
    args = parser.parse_args()

    if args.user_auth is not None:
        add_to_cart_random(args.user_auth)
        print(f"Successfully added random items to cart for connected user: {args.user_auth}")
    else:
        auth = login_with_id(args.user_id, args.file_path)
        add_to_cart_random(auth)
        print(f"Successfully logged in and added random items to cart")
