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

        print(f"GET Request - ID: {random_id}, UserID: {random_user_id}")
        print(f"Title: {data['title']}")
        print(f"Body: {data['body']}")
        print("\n")

    def test_post_request(self):
        random_user_id = 11
        random_id = random.randint(101, 110)
        payload = {
            "userId": random_user_id,
            "id": random_id,
            "title": "Luis Brito",
            "body": "Mental bom"
        }
        response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
        self.assertEqual(response.status_code, 201)

        print(f"POST Request - ID: {random_id}, UserID: {random_user_id}")
        print(f"Title: Luis Brito")
        print(f"Body: Mental bom")
        print("\n")

class APITestSuite2(unittest.TestCase):

    def test_put_request(self):
        random_user_id = 3
        random_id = random.randint(21, 30)  
        payload = {
            "userId": random_user_id,
            "id": random_id,
            "title": "mudando aqui",
            "body": "Corpo e saude"
        }
        response = requests.put(f"https://jsonplaceholder.typicode.com/posts/{random_id}", json=payload)
        self.assertEqual(response.status_code, 200)

        print(f"PUT Request - ID: {random_id}, UserID: {random_user_id}")
        print(f"Title: Mudando aqui")
        print(f"Body: Corpo e saude")
        print("\n")

    def test_delete_request(self):
        random_id = random.randint(31, 40)  
        response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{random_id}")
        self.assertEqual(response.status_code, 200)

        print(f"DELETE Request - ID: {random_id}")
        print("\n")

class APITestSuite3(unittest.TestCase):

    def test_another_get_request(self):
        random_user_id = 5
        random_id = random.randint(41, 50)  
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{random_id}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['userId'], random_user_id)

        print(f"GET Request (nova solicitação do luisão) - ID: {random_id}, UserID: {random_user_id}")
        print(f"Title: {data['title']}")
        print(f"Body: {data['body']}")
        print("\n")

if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(APITestSuite1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(APITestSuite2)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(APITestSuite3)

    test_runner = unittest.TextTestRunner(verbosity=3)

    test_runner.run(suite1)
    test_runner.run(suite2)
    test_runner.run(suite3)
