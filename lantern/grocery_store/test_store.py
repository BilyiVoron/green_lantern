import inject
import pytest
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


class TestUsers(Initializer):
    def test_create_user(self):
        resp = self.client.post(
            "/users",
            json={"name": "John Doe"}
        )
        assert resp.status_code == 201
        assert resp.json == {"user_id": 1}
        resp = self.client.post(
            "/users",
            json={"name": "Bohdan Dats'ko"}
        )
        assert resp.json == {"user_id": 2}

    def test_successful_get_user(self):
        resp = self.client.post(
            "/users",
            json={"name": "Bohdan Dats'ko"}
        )
        user_id = resp.json["user_id"]
        resp = self.client.get(f"/users/{user_id}")
        assert resp.status_code == 200
        assert resp.json == {"name": "Bohdan Dats'ko"}

    def test_get_unexistent_user(self):
        resp = self.client.get(f"/users/1")
        assert resp.status_code == 404
        assert resp.json == {"error": "No such user_id 1"}

    def test_successful_update_user(self):
        resp = self.client.post(
            "/users",
            json={"name": "John Doe"}
        )
        user_id = resp.json["user_id"]
        resp = self.client.put(
            f"/users/{user_id}",
            json={"name": "Johanna Doe"}
        )
        assert resp.status_code == 200
        assert resp.json == {"status": "success"}

    @pytest.mark.parametrize(
        "current_user_id,expected_user_id",
        ((1, 5),)
    )
    def test_update_unexistent_user(self, current_user_id, expected_user_id):
        resp = self.client.get(f"/users/{expected_user_id}")
        assert current_user_id != expected_user_id
        assert resp.status_code == 404
        assert resp.json == {"error": "No such user_id 5"}


class TestGoods(Initializer):
    def test_create_goods(self):
        resp = self.client.post(
            "/goods",
            json=[
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
        )
        assert resp.status_code == 201
        assert resp.json == {"numbers_of_items_created": 10}

    def test_get_good(self):
        self.client.post(
            "/goods",
            json=[
                {"name": "Chocolate_bar", "price": 10},
            ]
        )
        good_id = 1
        resp = self.client.get(f"/goods/{good_id}")
        assert resp.status_code == 200
        assert resp.json == {"name": "Chocolate_bar", "price": 10, "good_id": 1}

    def test_update_good(self):
        self.client.post(
            "/goods",
            json=[
                {"name": "Chocolate_bar", "price": 10},
            ]
        )
        good_id = 1
        resp = self.client.put(
            f"/goods/{good_id}",
            json={"name": "Chocolate_bar", "price": 11, "good_id": 1}
        )
        assert resp.status_code == 200
        assert resp.json == {"successfully_updated": 1}


class TestStores(Initializer):
    def test_create_store(self):
        resp = self.client.post(
            "/stores",
            json={"name": "Mad Cow", "location": "Lviv", "manager_id": 2}
        )
        assert resp.status_code == 201
        assert resp.json == {"store_id": 1}
        # resp = self.client.post(
        #     "/stores",
        #     json={"name": "Bohdan Dats'ko"}
        # )
        # assert resp.json == {"store_id": 2}

    def test_successful_get_store(self):
        resp = self.client.post(
            "/stores",
            json={"name": "Mad Cow", "location": "Lviv", "manager_id": 2}
        )
        store_id = resp.json["store_id"]
        resp = self.client.get(f"/stores/{store_id}")
        assert resp.status_code == 200
        assert resp.json == {"name": "Mad Cow", "location": "Lviv", "manager_id": 2}

    def test_get_unexistent_store(self):
        resp = self.client.get(f"/stores/1")
        assert resp.status_code == 404
        assert resp.json == {"error": "No such store_id 1"}

    def test_successful_update_store(self):
        resp = self.client.post(
            "/stores",
            json={"name": "Mad Cow", "location": "Lviv", "manager_id": 2}
        )
        store_id = resp.json["store_id"]
        resp = self.client.put(
            f"/stores/{store_id}",
            json={"name": "Local Taste", "location": "Lviv", "manager_id": 2}
        )
        assert resp.status_code == 200
        assert resp.json == {"status": "success"}

    @pytest.mark.parametrize(
        "current_store_id,expected_store_id",
        ((1, 5),)
    )
    def test_update_unexistent_store(self, current_store_id, expected_store_id):
        resp = self.client.get(f"/stores/{expected_store_id}")
        assert current_store_id != expected_store_id
        assert resp.status_code == 404
        assert resp.json == {"error": "No such store_id 5"}
