import requests
import unittest
import random

class APITestSuite1(unittest.TestCase):

    def test_get_request(self):
        random_user_id = 1
        random_id = random.randint(1, 10) 
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{random_id}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['userId'], random_user_id)

    def test_post_request(self):
        random_user_id = 2
        random_id = random.randint(11, 20)
        payload = {
            "userId": random_user_id,
            "id": random_id,
            "title": "Teste de post",
            "body": "Corpo do post"
        }
        response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
        self.assertEqual(response.status_code, 201)

class APITestSuite2(unittest.TestCase):

    def test_put_request(self):
        random_user_id = 3
        random_id = random.randint(21, 30)  
        payload = {
            "userId": random_user_id,
            "id": random_id,
            "title": "Teste de put",
            "body": "Corpo do put"
        }
        response = requests.put(f"https://jsonplaceholder.typicode.com/posts/{random_id}", json=payload)
        self.assertEqual(response.status_code, 200)

    def test_delete_request(self):
        random_id = random.randint(31, 40)  
        response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{random_id}")
        self.assertEqual(response.status_code, 200)

class APITestSuite3(unittest.TestCase):

    def test_another_get_request(self):
        random_user_id = 5
        random_id = random.randint(41, 50)  
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{random_id}")
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
