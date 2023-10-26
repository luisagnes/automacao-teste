import requests
import unittest
import random

class APITestSuite1(unittest.TestCase):

    def test_get_request(self):
        random_user_id = 1
        random_id = random.randint(1, 20)  
        response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{random_id}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['userId'], random_user_id)

        print(f"GET Request - ID: {random_id}, UserID: {random_user_id}")
        print(f"Title: {data['title']}")
        print(f"Completed: {data['completed']}")
        print("\n")

    def test_post_request(self):
        random_user_id = 11
        random_id = random.randint(201, 220)  
        payload = {
            "userId": random_user_id,
            "id": random_id,
            "title": "Teste do Luis aqui",
            "completed": False
        }
        response = requests.post("https://jsonplaceholder.typicode.com/todos", json=payload)
        self.assertEqual(response.status_code, 201)

        print(f"POST Request - ID: {random_id}, UserID: {random_user_id}")
        print("Title: Teste do Luis aqui")
        print("Completed: False")
        print("\n")

class APITestSuite2(unittest.TestCase):

    def test_put_request(self):
        random_user_id = 3
        random_id = random.randint(41, 60)  
        payload = {
            "userId": random_user_id,
            "id": random_id,
            "title": "mudando aqui",
            "completed": True
        }
        response = requests.put(f"https://jsonplaceholder.typicode.com/todos/{random_id}", json=payload)
        self.assertEqual(response.status_code, 200)

        print(f"PUT Request - ID: {random_id}, UserID: {random_user_id}")
        print("Title: mudando aqui")
        print("Completed: True")
        print("\n")

    def test_delete_request(self):
        random_id = random.randint(61, 80)  
        response = requests.delete(f"https://jsonplaceholder.typicode.com/todos/{random_id}")
        self.assertEqual(response.status_code, 200)

        print(f"DELETE Request - ID: {random_id}")
        print("\n")

class APITestSuite3(unittest.TestCase):

    def test_another_get_request(self):
        random_user_id = 5
        random_id = random.randint(81, 100)  
        response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{random_id}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['userId'], random_user_id)

        print(f"GET Request (nova solicitação) - ID: {random_id}, UserID: {random_user_id}")
        print(f"Title: {data['title']}")
        print(f"Completed: {data['completed']}")
        print("\n")

if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(APITestSuite1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(APITestSuite2)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(APITestSuite3)

    test_runner = unittest.TextTestRunner(verbosity=3)

    test_runner.run(suite1)
    test_runner.run(suite2)
    test_runner.run(suite3)



