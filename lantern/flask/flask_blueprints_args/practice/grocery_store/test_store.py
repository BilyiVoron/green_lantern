import inject

from fake_storage import FakeStorage
from store_app import make_app


def configure_test(binder):
    db = FakeStorage()
    binder.bind("DB", db)


class Initializer:
    def setup(self):
        inject.clear_and_configure(configure_test)
        app = make_app()
        app.config["TESTING"] = True
        with app.test_client() as client:
            self.client = client
            self.user_route = "/users"
            self.good_route = "/goods"
            self.store_route = "/stores"


class TestUsers(Initializer):
    TEST_USER = {"name": "John Doe"}

    def _post_user(self):
        return self.client.post(self.user_route, json=self.TEST_USER)

    def test_create_user(self):
        resp = self._post_user()
        assert resp.status_code == 201
        assert resp.json == {"user_id": 1}

        resp = self._post_user()
        assert resp.status_code == 201
        assert resp.json == {"user_id": 2}

    def test_successful_get_user(self):
        resp = self._post_user()
        user_id = resp.json["user_id"]
        resp = self.client.get(f"{self.user_route}/{user_id}")
        assert resp.status_code == 200
        assert resp.json == {"name": "John Doe"}

    def test_get_nonexistent_user(self):
        self._post_user()
        user_id = 3
        resp = self.client.get(f"{self.user_route}/{user_id}")
        assert resp.status_code == 404
        assert resp.json == {"error": "No such user_id 3"}

    def test_successful_update_user(self):
        resp = self._post_user()
        user_id = resp.json["user_id"]
        resp = self.client.put(
            f"{self.user_route}/{user_id}", json={"name": "Johanna Doe"}
        )
        assert resp.status_code == 200
        assert resp.json == {"status": "success"}

    def test_update_nonexistent_user(self):
        self._post_user()
        user_id = 5
        resp = self.client.put(
            f"{self.user_route}/{user_id}", json={"name": "Johanna Doe"}
        )
        assert resp.status_code == 404
        assert resp.json == {"error": "No such user_id 5"}

    def test_successful_delete_user(self):
        resp = self._post_user()
        user_id = resp.json["user_id"]
        resp = self.client.delete(f"{self.user_route}/{user_id}")
        assert resp.status_code == 200
        assert resp.json == {"status": "success"}

    def test_delete_nonexistent_user(self):
        self._post_user()
        user_id = 15
        resp = self.client.delete(f"{self.user_route}/{user_id}")
        assert resp.status_code == 404
        assert resp.json == {"error": "No such user_id 15"}


class TestGoods(Initializer):
    TEST_GOODS = (
        ("Chocolate_bar", 10),
        ("Milk_jar", 15),
        ("Ice-cream", 25),
        ("Honey", 50),
        ("Cheese", 26),
        ("Beetroot", 2),
        ("Potato", 3.5),
        ("Sugar", 7.8),
        ("Salt", 3),
        ("Water", 6),
    )

    def _post_goods(self):
        return self.client.post(
            self.good_route,
            json=[{"name": name, "price": price} for name, price in self.TEST_GOODS],
        )

    def test_create_goods(self):
        resp = self._post_goods()
        assert resp.status_code == 201
        assert resp.json == {"number of items created": 10}

    def test_get_goods(self):
        self._post_goods()
        resp = self.client.get(self.good_route)
        assert resp.status_code == 200
        assert resp.json == [
            {"name": "Chocolate_bar", "price": 10, "id": 1},
            {"name": "Milk_jar", "price": 15, "id": 2},
            {"name": "Ice-cream", "price": 25, "id": 3},
            {"name": "Honey", "price": 50, "id": 4},
            {"name": "Cheese", "price": 26, "id": 5},
            {"name": "Beetroot", "price": 2, "id": 6},
            {"name": "Potato", "price": 3.5, "id": 7},
            {"name": "Sugar", "price": 7.8, "id": 8},
            {"name": "Salt", "price": 3, "id": 9},
            {"name": "Water", "price": 6, "id": 10},
        ]


class TestStore(Initializer):
    def _post_store(self):
        resp = self.client.post(self.user_route, json={"name": "John Doe"})
        user_id = resp.json["user_id"]
        return self.client.post(
            self.store_route,
            json={"name": "Mad Cow", "location": "Lviv", "manager_id": user_id},
        )

    def test_create_store(self):
        resp = self._post_store()
        assert resp.status_code == 201
        assert resp.json == {"store_id": 1}

    def test_successful_get_store(self):
        resp = self._post_store()
        store_id = resp.json["store_id"]
        resp = self.client.get(f"{self.store_route}/{store_id}")
        assert resp.status_code == 200
        assert resp.json == {"name": "Mad Cow", "location": "Lviv", "manager_id": 1}

    def test_get_nonexistent_store(self):
        self._post_store()
        resp = self.client.get(f"{self.store_route}/2")
        assert resp.status_code == 404
        assert resp.json == {"error": "No such store_id 2"}

    def test_successful_update_store(self):
        resp = self._post_store()
        store_id = resp.json["store_id"]
        resp = self.client.put(
            f"{self.store_route}/{store_id}",
            json={"name": "Local Taste", "location": "Lviv", "manager_id": 1},
        )
        assert resp.status_code == 200
        assert resp.json == {"status": "success"}

    def test_update_store_with_nonexistent_user(self):
        resp = self._post_store()
        store_id = resp.json["store_id"]
        resp = self.client.put(
            f"{self.store_route}/{store_id}",
            json={"name": "Local Taste", "location": "Lviv", "manager_id": 2},
        )
        assert resp.status_code == 404
        assert resp.json == {"error": "No such user_id 2"}

    def test_update_nonexistent_store(self):
        self._post_store()
        store_id = 5
        resp = self.client.put(
            f"{self.store_route}/{store_id}",
            json={"name": "Local Taste", "location": "Lviv", "manager_id": 1},
        )
        assert resp.status_code == 404
        assert resp.json == {"error": "No such store_id 5"}

    def test_successful_delete_store(self):
        resp = self._post_store()
        store_id = resp.json["store_id"]
        resp = self.client.delete(f"{self.store_route}/{store_id}")
        assert resp.status_code == 200
        assert resp.json == {"status": "success"}

    def test_delete_nonexistent_store(self):
        self._post_store()
        store_id = 7
        resp = self.client.delete(f"{self.store_route}/{store_id}")
        assert resp.status_code == 404
        assert resp.json == {"error": "No such store_id 7"}
