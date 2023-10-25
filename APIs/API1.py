import requests
import unittest
import random

class APITestSuite1(unittest.TestCase):

    def test_get_request(self):
        random_user_id = 1
        random_id = random.randint(1, 20)  # Seleciona ID entre 1 e 20
        response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{random_id}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['userId'], random_user_id)

    def test_post_request(self):
        random_user_id = 2
        random_id = random.randint(21, 40)  # Seleciona ID entre 21 e 40
        payload = {
            "userId": random_user_id,
            "id": random_id,
            "title": "Teste de post",
            "completed": False
        }
        response = requests.post("https://jsonplaceholder.typicode.com/todos", json=payload)
        self.assertEqual(response.status_code, 201)

class APITestSuite2(unittest.TestCase):

    def test_put_request(self):
        random_user_id = 3
        random_id = random.randint(41, 60)  # Seleciona ID entre 41 e 60
        payload = {
            "userId": random_user_id,
            "id": random_id,
            "title": "Teste de put",
            "completed": True
        }
        response = requests.put(f"https://jsonplaceholder.typicode.com/todos/{random_id}", json=payload)
        self.assertEqual(response.status_code, 200)

    def test_delete_request(self):
        random_id = random.randint(61, 80)  # Seleciona ID entre 61 e 80
        response = requests.delete(f"https://jsonplaceholder.typicode.com/todos/{random_id}")
        self.assertEqual(response.status_code, 200)

class APITestSuite3(unittest.TestCase):

    def test_another_get_request(self):
        random_user_id = 5
        random_id = random.randint(81, 100)  # Seleciona ID entre 81 e 100
        response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{random_id}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['userId'], random_user_id)

if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(APITestSuite1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(APITestSuite2)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(APITestSuite3)

    test_runner = unittest.TextTestRunner(verbosity=3)

    test_runner.run(suite1)
    test_runner.run(suite2)
    test_runner.run(suite3)



