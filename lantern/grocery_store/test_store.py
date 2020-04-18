import inject
from store_app import app
from fake_storage import FakeStorage


def configure_test(binder):
    db = FakeStorage()
    binder.bind("DB", db)


class Initializer:
    def setup(self):
        inject.clear_and_configure(configure_test)

        app.config["TESTING"] = True
        with app.test_client() as client:
            self.client = client
            self.user = self.setup_user()
            self.user_route = "/users"
            self.goods = self.setup_goods()
            self.good_route = "/goods"
            self.stores = self.setup_store()
            self.store_route = "/stores"

    @staticmethod
    def setup_user():
        return {"name": "John Doe"}

    @staticmethod
    def setup_goods():
        return [
            {"name": "Chocolate_bar", "price": 10},
            {"name": "Milk_jar", "price": 15},
            {"name": "Ice-cream", "price": 25},
            {"name": "Honey", "price": 50},
            {"name": "Cheese", "price": 26},
            {"name": "Beetroot", "price": 2},
            {"name": "Potato", "price": 3.5},
            {"name": "Sugar", "price": 7.8},
            {"name": "Salt", "price": 3},
            {"name": "Water", "price": 6},
        ]

    @staticmethod
    def setup_store():
        client = app.test_client()
        user_route = "/users"
        resp = client.post(user_route, json={"name": "John Doe"})
        user_id = resp.json["user_id"]
        return {"name": "Mad Cow", "location": "Lviv", "manager_id": user_id}


class TestUsers(Initializer):
    def test_create_user(self):
        resp = self.client.post(self.user_route, json=self.user)
        assert resp.status_code == 201
        assert resp.json == {"user_id": 2}
        resp = self.client.post(self.user_route, json=self.user)
        assert resp.status_code == 201
        assert resp.json == {"user_id": 3}

    def test_successful_get_user(self):
        resp = self.client.post(self.user_route, json=self.user)
        user_id = resp.json["user_id"]
        resp = self.client.get(f"{self.user_route}/{user_id}")
        assert resp.status_code == 200
        assert resp.json == {"name": "John Doe"}

    def test_get_nonexistent_user(self):
        self.client.post(self.user_route, json=self.user)
        resp = self.client.get(f"{self.user_route}/3")
        assert resp.status_code == 404
        assert resp.json == {"error": "No such user_id 3"}

    def test_successful_update_user(self):
        resp = self.client.post(self.user_route, json=self.user)
        user_id = resp.json["user_id"]
        resp = self.client.put(
            f"{self.user_route}/{user_id}", json={"name": "Johanna Doe"}
        )
        assert resp.status_code == 200
        assert resp.json == {"status": "success"}

    def test_update_nonexistent_user(self):
        self.client.post(self.user_route, json=self.user)
        user_id = 5
        resp = self.client.put(
            f"{self.user_route}/{user_id}", json={"name": "Johanna Doe"}
        )
        assert resp.status_code == 404
        assert resp.json == {"error": "No such user_id 5"}

    def test_successful_delete_user(self):
        resp = self.client.post(self.user_route, json=self.user)
        user_id = resp.json["user_id"]
        resp = self.client.delete(f"{self.user_route}/{user_id}")
        assert resp.status_code == 200
        assert resp.json == {"status": "success"}

    def test_delete_nonexistent_user(self):
        self.client.post(self.user_route, json=self.user)
        user_id = 15
        resp = self.client.delete(f"{self.user_route}/{user_id}")
        assert resp.status_code == 404
        assert resp.json == {"error": "No such user_id 15"}


class TestGoods(Initializer):
    def test_create_goods(self):
        resp = self.client.post(self.good_route, json=self.goods)
        assert resp.status_code == 201
        assert resp.json == {"numbers_of_items_created": 10}

    def test_get_one_good(self):
        self.client.post(self.good_route, json=self.goods)
        good_id = 2
        resp = self.client.get(f"{self.good_route}/{good_id}")
        assert resp.status_code == 200
        assert resp.json == {"name": "Milk_jar", "price": 15, "good_id": good_id}
        good_id = 1
        resp = self.client.get(f"{self.good_route}/{good_id}")
        assert resp.status_code == 200
        assert resp.json == {"name": "Chocolate_bar", "price": 10, "good_id": good_id}

    def test_get_all_goods(self):
        self.client.post(self.good_route, json=self.goods)
        resp = self.client.get(self.good_route, json=self.goods)
        assert resp.status_code == 200
        assert resp.json == [
            {"name": "Chocolate_bar", "price": 10, "good_id": 1},
            {"name": "Milk_jar", "price": 15, "good_id": 2},
            {"name": "Ice-cream", "price": 25, "good_id": 3},
            {"name": "Honey", "price": 50, "good_id": 4},
            {"name": "Cheese", "price": 26, "good_id": 5},
            {"name": "Beetroot", "price": 2, "good_id": 6},
            {"name": "Potato", "price": 3.5, "good_id": 7},
            {"name": "Sugar", "price": 7.8, "good_id": 8},
            {"name": "Salt", "price": 3, "good_id": 9},
            {"name": "Water", "price": 6, "good_id": 10},
        ]

    def test_update_one_good(self):
        self.client.post(self.good_route, json=self.goods)
        good_id = 1
        resp = self.client.put(
            f"{self.good_route}/{good_id}",
            json={"name": "Cocoa", "price": 11, "good_id": good_id},
        )
        assert resp.status_code == 200
        assert resp.json == {"successfully_updated": 1}
        good_id = 2
        resp = self.client.put(
            f"{self.good_route}/{good_id}",
            json={"name": "Sour-cream", "price": 15, "good_id": good_id},
        )
        assert resp.status_code == 200
        assert resp.json == {"successfully_updated": 1}

    def test_update_some_goods(self):
        self.client.post(self.good_route, json=self.goods)
        resp = self.client.put(
            f"{self.good_route}",
            json=[
                {"name": "Cocoa", "price": 7.86, "good_id": 1},
                {"name": "Sour-cream", "price": 4.45, "good_id": 2},
                {"name": "Ice-cream", "price": 25, "good_id": 3},
                {"name": "Honey", "price": 50, "good_id": 4},
                {"name": "Cheese", "price": 26, "good_id": 5},
                {"name": "Cauliflower", "price": 3.68, "good_id": 6},
                {"name": "Potato", "price": 3.5, "good_id": 7},
                {"name": "Sugar", "price": 7.8, "good_id": 8},
                {"name": "Salt", "price": 3, "good_id": 9},
                {"name": "Water", "price": 6, "good_id": 10},
                {"name": "Sugar", "price": 7.8, "good_id": 11},
                {"name": "Salt", "price": 3, "good_id": 12},
                {"name": "Water", "price": 6, "good_id": 13},
            ],
        )
        assert resp.status_code == 200
        assert resp.json == {
            "successfully_updated": 10,
            "errors": {"no such id in goods": [11, 12, 13]},
        }

    def test_successful_delete_good(self):
        self.client.post(self.good_route, json=self.goods)
        good_id = 1
        resp = self.client.delete(f"{self.good_route}/{good_id}")
        assert resp.status_code == 200
        assert resp.json == {"status": "success"}

    def test_delete_some_goods(self):
        self.client.post(self.good_route, json=self.goods)
        resp = self.client.delete(
            f"{self.good_route}",
            json=[
                {"name": "Cocoa", "price": 7.86, "good_id": 1},
                {"name": "Sour-cream", "price": 4.45, "good_id": 2},
                {"name": "Ice-cream", "price": 25, "good_id": 3},
                {"name": "Sugar", "price": 7.8, "good_id": 11},
                {"name": "Salt", "price": 3, "good_id": 12},
                {"name": "Water", "price": 6, "good_id": 13},
            ],
        )
        assert resp.status_code == 200
        assert resp.json == {
            "successfully_deleted": 3,
            "errors": {"no such id in goods": [11, 12, 13]},
        }


class TestStores(Initializer):
    def test_create_store(self):
        resp = self.client.post(self.store_route, json=self.stores)
        assert resp.status_code == 201
        assert resp.json == {"store_id": 1}

    def test_successful_get_store(self):
        resp = self.client.post(self.store_route, json=self.stores)
        store_id = resp.json["store_id"]
        resp = self.client.get(f"{self.store_route}/{store_id}")
        assert resp.status_code == 200
        assert resp.json == {"name": "Mad Cow", "location": "Lviv", "manager_id": 1}

    def test_get_nonexistent_store(self):
        self.client.post(self.store_route, json=self.stores)
        resp = self.client.get(f"{self.store_route}/2")
        assert resp.status_code == 404
        assert resp.json == {"error": "No such store_id 2"}

    def test_successful_update_store(self):
        resp = self.client.post(self.store_route, json=self.stores)
        store_id = resp.json["store_id"]
        resp = self.client.put(
            f"{self.store_route}/{store_id}",

            json={"name": "Local Taste", "location": "Lviv", "manager_id": 1},
        )
        assert resp.status_code == 200
        assert resp.json == {"status": "success"}

    def test_update_store_with_nonexistent_user(self):
        resp = self.client.post(self.store_route, json=self.stores)
        store_id = resp.json["store_id"]
        resp = self.client.put(
            f"{self.store_route}/{store_id}",

            json={"name": "Local Taste", "location": "Lviv", "manager_id": 2},
        )
        assert resp.status_code == 404
        assert resp.json == {"error": "No such user_id 2"}

    def test_update_nonexistent_store(self):
        self.client.post(self.store_route, json=self.stores)
        store_id = 5
        resp = self.client.put(
            f"{self.store_route}/{store_id}",
            json={"name": "Local Taste", "location": "Lviv", "manager_id": 1},
        )
        assert resp.status_code == 404
        assert resp.json == {"error": "No such store_id 5"}

    def test_successful_delete_store(self):
        resp = self.client.post(self.store_route, json=self.stores)
        store_id = resp.json["store_id"]
        resp = self.client.delete(f"{self.store_route}/{store_id}")
        assert resp.status_code == 200
        assert resp.json == {"status": "success"}

    def test_delete_nonexistent_store(self):
        store_id = 7
        resp = self.client.delete(f"{self.store_route}/{store_id}")
        assert resp.status_code == 404
        assert resp.json == {"error": "No such store_id 7"}
