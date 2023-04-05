import requests
from modules.cart import add_to_cart_random
from modules.user import random_login


def main():
    auth = random_login()
    nb_items = add_to_cart_random(auth)
    if nb_items == 0:
        print('No items were added to the cart, aborting purchase')
        return

    url = 'http://127.0.0.1:5184/addPurchase'
    response = requests.post(url, headers={'Authorization': auth})
    if response.ok:
        print(f'Normal purchase successful')
    elif response.status_code == 400:
        print('Not enough items for normal purchase')
    elif response.status_code == 401:
        print('Login error in normal purchase')
        exit(1)
    else:
        print(f'Error in normal purchase: {response.status_code}')
        exit(1)


if __name__ == '__main__':
    main()
