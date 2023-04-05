import random
from modules.user import random_login
from modules.cart import add_to_cart_random, clear_cart


def main():
    auth = random_login()
    add_to_cart_random(auth)
    print(f"Successfully logged in and added random items to cart")
    if random.randint(0, 1) == 1:
        clear_cart(auth)


if __name__ == '__main__':
    main()


