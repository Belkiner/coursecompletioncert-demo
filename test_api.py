import unittest
from app import app, _tasks


class TaskApiTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        _tasks.clear()

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})

    def test_list_tasks_initially_empty(self):
        response = self.client.get("/tasks")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"tasks": []})

    def test_create_task(self):
        response = self.client.post("/tasks", json={"title": "Demo task"})
        self.assertEqual(response.status_code, 201)
        task = response.get_json()["task"]
        self.assertEqual(task["title"], "Demo task")
        self.assertFalse(task["completed"])
        self.assertEqual(task["id"], 1)

    def test_reject_blank_title(self):
        response = self.client.post("/tasks", json={"title": "   "})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()["error"], "validation_error")

    def test_reject_missing_title(self):
        response = self.client.post("/tasks", json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()["error"], "validation_error")

    def test_reject_non_json_request(self):
        response = self.client.post("/tasks", data="title=demo")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()["error"], "invalid_content_type")


if __name__ == "__main__":
    unittest.main()
