import requests
import random

url = "http://127.0.0.1:5182/addCartItem"


def add_to_cart(auth_token, item_id, item_qty):
    data = {
        "item_id": item_id,
        "item_quantity": item_qty
    }
    # TODO test auth= or this: headers = {'Authorization': auth_token},
    response = requests.post(url, json=data, auth=auth_token)
    http_status_code = response.status_code

    if http_status_code == 200:
        print(f'Added {item_qty} of Item: {item_id} to cart for a random user:')
        return
    elif http_status_code == 401:
        print('Login error in normal add cart')
        exit(1)
    else:
        print('Error in normal add cart')
        exit(1)


def add_to_cart_random(auth_token):
    nb_items = random.randint(1, 3)

    for _ in range(nb_items):
        item_id = random.randint(1, 1000)
        item_qty = random.randint(1, 10)

        add_to_cart(auth_token, item_id, item_qty)
