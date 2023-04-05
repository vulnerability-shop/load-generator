import requests
from modules.cart import add_to_cart_random
from modules.user import random_login


def main():
    auth = random_login()
    add_to_cart_random(auth)

    url = 'http://127.0.0.1:5184/addPurchase'
    response = requests.post(url, headers={'Authorization': auth})
    if response.ok:
        print(f'Normal purchase successful')
    elif response.status_code == 401:
        print('Login error in normal purchase')
        exit(1)
    else:
        print(f'Error in normal purchase: {response.status_code}')
        exit(1)


if __name__ == '__main__':
    main()
