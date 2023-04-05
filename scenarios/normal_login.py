from modules.user import random_login


def main ():
    # Run fetch user for a random user id
    auth = random_login()
    print(f'Random user logged in, returned token: {auth}')


if __name__ == '__main__':
    main()
