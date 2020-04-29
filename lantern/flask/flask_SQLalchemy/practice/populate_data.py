import csv


def get_users():
    with open("users.csv") as f:
        reader = csv.DictReader(f)
        users = [user for user in reader]
    return users
