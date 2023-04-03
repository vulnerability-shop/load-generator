import argparse
from modules.login import *


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--user_id", type=int, required=False, default=-1, help="UserId, if null, will login as random")
    parser.add_argument("--file_path", type=str, required=False, help="user_migration csv path, if null uses default")
    parser.add_argument("--username", type=str, required=False, help="Manual username input")
    parser.add_argument("--password", type=str, required=False, help="Manual password input")
    args = parser.parse_args()

    if args.username is not None and args.password is not None:
        # login with manual username and password
        auth = login_with_credentials(args.username, args.password)
    else:
        # Run fetch user for a random user id
        auth = login_with_id(args.user_id, args.file_path)
    print(auth)

