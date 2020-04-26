from itertools import count

from errors import NoSuchUserError, NoSuchGoodError, NoSuchStoreError


class Repository:
    def __init__(self):
        self._db = {}
        self._id_counter = count(1)

    def add(self, item):
        item_id = next(self._id_counter)
        self._db[item_id] = item
        return item_id


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


class FakeUsers(Repository):
    def get_user_by_id(self, user_id):
        try:
            return self._db[user_id]
        except KeyError:
            raise NoSuchUserError(user_id)

    def update_user_by_id(self, user_id, user):
        if user_id in self._db:
            self._db[user_id] = user
        else:
            raise NoSuchUserError(user_id)

    def remove_user_by_id(self, user_id):
        if user_id in self._db:
            self._db.pop(user_id)
        else:
            raise NoSuchUserError(user_id)


class FakeGoods(Repository):
    def add_many(self, items):
        for item in items:
            self.add(item)
        return len(items)

    # def get_good_by_id(self, good_id):
    #     # return self._goods.get(good_id, {"error": f"No such good_id {good_id}"})
    #     try:
    #         return self._db[good_id]
    #     except KeyError:
    #         raise NoSuchGoodError(good_id)

    def get_all(self):
        return [{**item, "id": item_id} for item_id, item in self._db.items()]

    # def get_goods(self):
    #     return list(self._db.values())
    #
    # def update_good_by_id(self, good_id, good):
    #     if good_id in self._db:
    #         self._db[good_id].update(good)
    #     else:
    #         raise NoSuchGoodError(good_id)
    #
    # def update_goods(self, goods):
    #     success, error = 0, []
    #     for upd_good in goods:
    #         good_id = upd_good["good_id"]
    #         if self._db.get(good_id, None):
    #             success += 1
    #             self._db[good_id] = upd_good
    #         else:
    #             error.append(upd_good["good_id"])
    #     return success, error
    #
    # def remove_good_by_id(self, good_id):
    #     if good_id in self._db:
    #         self._db.pop(good_id, {})
    #     else:
    #         raise NoSuchGoodError(good_id)
    #
    # def remove_goods(self, goods):
    #     success, error = 0, []
    #     for del_good in goods:
    #         good_id = del_good["good_id"]
    #         if self._db.pop(good_id, {}):
    #             success += 1
    #             self._db[good_id] = del_good
    #         else:
    #             error.append(del_good["good_id"])
    #     return success, error


class FakeStores(Repository):
    def get_store_by_id(self, store_id):
        try:
            return self._db[store_id]
        except KeyError:
            raise NoSuchStoreError(store_id)

    def get_stores_by_name(self, name):
        for store_id, store_data in self._db.items():
            if name == store_data["name"]:
                return store_data
        try:
            return self._db[name]
        except KeyError:
            raise NoSuchStoreError(name)

    def update_store_by_id(self, store_id, store):
        if store_id in self._db:
            self._db[store_id] = store
        else:
            raise NoSuchStoreError(store_id)

    def remove_store_by_id(self, store_id):
        if store_id in self._db:
            self._db.pop(store_id)
        else:
            raise NoSuchStoreError(store_id)
