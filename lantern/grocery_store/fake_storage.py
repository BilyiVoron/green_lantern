from itertools import count
from store_app import NoSuchUserError, NoSuchStoreError


class FakeStorage:
    def __init__(self):
        self._users = FakeUsers()
        self._goods = FakeGoods()
        self._stores = FakeStores()

    @property
    def users(self):
        return self._users

    @property
    def goods(self):
        return self._goods

    @property
    def stores(self):
        return self._stores


class FakeUsers:
    def __init__(self):
        self._users = {}
        self._id_counter = count(1)

    def add(self, user):
        user_id = next(self._id_counter)
        self._users[user_id] = user
        return user_id

    def get_user_by_id(self, user_id):
        try:
            return self._users[user_id]
        except KeyError:
            raise NoSuchUserError(user_id)

    def update_user_by_id(self, user_id, user):
        if user_id in self._users:
            self._users[user_id] = user
        else:
            raise NoSuchUserError(user_id)

    def remove_user_by_id(self, user_id):
        if user_id in self._users:
            self._users.pop(user_id)
        else:
            raise NoSuchUserError(user_id)


class FakeGoods:
    def __init__(self):
        self._goods = {}
        self._id_counter = count(1)

    def add(self, goods):
        for good_id, good in enumerate(goods, start=1):
            good["good_id"] = good_id
            self._goods[good_id] = good
        return self._goods

    def get_good_by_id(self, good_id):
        return self._goods.get(good_id, {})

    def get_goods(self):
        return list(self._goods.values())

    def update_good_by_id(self, good_id, good):
        if good_id in self._goods:
            self._goods[good_id].update(good)

    def update_goods(self, goods):
        success, error = 0, []
        for upd_good in goods:
            good_id = upd_good["good_id"]
            if self._goods.get(good_id, None):
                success += 1
                self._goods[good_id] = upd_good
            else:
                error.append(upd_good["good_id"])
        return success, error

    def remove_good_by_id(self, good_id):
        if good_id in self._goods:
            self._goods.pop(good_id, {})
        else:
            raise KeyError

    def remove_goods(self, goods):
        success, error = 0, []
        for del_good in goods:
            good_id = del_good["good_id"]
            if self._goods.pop(good_id, {}):
                success += 1
                self._goods[good_id] = del_good
            else:
                error.append(del_good["good_id"])
        return success, error


class FakeStores:
    def __init__(self):
        self._stores = {}
        self._id_counter = count(1)

    def add(self, store):
        store_id = next(self._id_counter)
        self._stores[store_id] = store
        return store_id

    def get_store_by_id(self, store_id):
        try:
            return self._stores[store_id]
        except KeyError:
            raise NoSuchStoreError(store_id)

    def update_store_by_id(self, store_id, store):
        if store_id in self._stores:
            self._stores[store_id] = store
        else:
            raise NoSuchStoreError(store_id)

    def remove_store_by_id(self, store_id):
        if store_id in self._stores:
            self._stores.pop(store_id)
        else:
            raise NoSuchStoreError(store_id)
