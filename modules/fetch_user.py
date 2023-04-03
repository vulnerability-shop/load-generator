#!/usr/bin/env python3
# Download the user migration csv: # https://github.com/vulnerability-shop/vulnerability-shop/blob/main/postgresql/migrations/import_data_Customer.csv
# to use, run: python fetch_user.py --userId <id> --filePath <FILE_PATH>, don't pass id for a random user

import csv
import random
import argparse

if __name__ == "__main__":
    userId = -1
    usersMigration = "../../vulnerability-shop/postgresql/migrations/import_data_Customer.csv";

    parser = argparse.ArgumentParser()
    parser.add_argument("--userId", type=int, required=False, help="UserId, if null, will login as random")
    parser.add_argument("--filePath", type=str, required=False, help="user_migration csv path, if null uses default")

    args = parser.parse_args()

    if args.filePath is not None:
        usersMigration = args.filePath

    with open(usersMigration, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        if args.userId is not None:
            row = list(csvreader)[args.userId]
        else:
            row = random.choice(list(csvreader))
        print(row[2] + ', ' + row[3])
