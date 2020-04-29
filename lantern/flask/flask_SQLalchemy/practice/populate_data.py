import csv


def get_users():
    with open("users.csv") as f:
        reader = csv.DictReader(f)
        users = [user for user in reader]
    return users


def get_goods():
    with open("goods.csv") as f:
        reader = csv.DictReader(f)
        goods = [good for good in reader]
    return goods


def get_stores():
    with open("stores.csv") as f:
        reader = csv.DictReader(f)
        stores = [store for store in reader]
    return stores
