import requests
import random
import json

url = 'http://127.0.0.1:5182/addCartItem'


def add_to_cart(auth_token, item_id, item_qty):
    data = {
        'itemId': item_id,
        'itemQuantity': item_qty
    }
    response = requests.post(url, json=data, headers={'Authorization': auth_token})
    if response.ok:
        print(f'Added {item_qty} of Item: {item_id} to cart for User: {json.loads(response.text)["customerId"]}')
    elif response.status_code == 401:
        print('Login error in normal add cart')
        exit(1)
    else:
        print('Error in normal add cart')
        exit(1)


def add_to_cart_random(auth_token):
    cart_items_url = 'http://127.0.0.1:5181/getItems'
    response = requests.get(cart_items_url)
    if not response.ok:
        print('Error fetching items in normal add cart')
    items = json.loads(response.text)['data']

    nb_items = random.randint(1, 3)
    for _ in range(nb_items):
        item_id = random.randint(1, len(items))
        item_qty = random.randint(1, items[item_id]['stock'])

        add_to_cart(auth_token, item_id, item_qty)
