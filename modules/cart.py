import requests
import random
import json


def add_to_cart(auth_token, item_id, item_qty):
    url = 'http://127.0.0.1:5182/addCartItem'
    data = {
        'itemId': item_id,
        'itemQuantity': item_qty
    }
    response = requests.post(url, json=data, headers={'Authorization': auth_token})
    if response.ok:
        print(f'Added {item_qty} of Item: {item_id} to cart for User: {json.loads(response.text)["customerId"]}')
    elif response.status_code == 401:
        print('Login error in add to cart')
        exit(1)
    else:
        print('Error in add to cart')
        exit(1)


def add_to_cart_random(auth_token):
    url = 'http://127.0.0.1:5181/getItems'
    response = requests.get(url)
    if not response.ok:
        print('Error fetching items in random add cart')
    items = json.loads(response.text)['data']

    nb_items = random.randint(1, 3)
    items_added = 0
    for _ in range(nb_items):
        item_id = random.randint(1, len(items))
        for item in items:
            if item['id'] == item_id:
                item_stock = item['stock']
                break
        if item_stock <= 0:
            continue
        item_qty = random.randint(1, item_stock)
        add_to_cart(auth_token, item_id, item_qty)
        items_added += 1
    return items_added


def clear_cart(auth_token):
    url = 'http://127.0.0.1:5182/clearUserCart'
    response = requests.delete(url, headers={'Authorization': auth_token})
    if response.ok:
        print(f'Cart cleared for User: {auth_token}')
    else:
        print(f'Error clearing cart for User: {auth_token}')
        exit(1)


def update_cart_item(auth_token, item_id, item_qty):
    url = 'http://127.0.0.1:5182/updateCartItem'
    data = {
        'itemId': item_id,
        'itemQuantity': item_qty
    }
    response = requests.put(url, json=data, headers={'Authorization': auth_token})
    if response.ok:
        print(f'Added {item_qty} of Item: {item_id} to cart for User: {json.loads(response.text)["customerId"]}')
    elif response.status_code == 401:
        print('Login error in cart update')
        exit(1)
    else:
        print('Error in cart update')
        exit(1)
