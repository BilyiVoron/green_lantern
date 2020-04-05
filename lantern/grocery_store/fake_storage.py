from itertools import count
from store_app import NoSuchUserError


class FakeStorage:
    def __init__(self):
        self._users = FakeUsers()
        self._goods = FakeGoods()

    @property
    def users(self):
        return self._users

    @property
    def goods(self):
        return self._goods


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


class FakeGoods:
    def __init__(self):
        self._goods = []
        self._id_counter = count(1)

    def add(self, goods):
        for good in goods:
            self._goods.append(good)
        return len(self._goods)

    def get_good_by_id(self, good_id):
        return self._goods[good_id]

    def update_good_by_id(self, good_id, good):
        if good_id in self._goods:
            self._goods[good_id] = good

