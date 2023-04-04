import csv
import random


def fetch_user_credentials(user_id: int = -1, users_migration: str = None):
    if users_migration is None:
        users_migration = '../../vulnerability-shop/postgresql/migrations/import_data_Customer.csv'
    with open(users_migration, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        if user_id != -1:
            row = list(csvreader)[user_id]
        else:
            row = random.choice(list(csvreader))
        return row[1], row[2]
