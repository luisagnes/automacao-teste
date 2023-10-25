import requests
import unittest
import random

class APITestSuite(unittest.TestCase):

    def test_user_request(self):
        random_id = random.randint(1, 10)  
        random_id2 = random.randint(1, 10)
        random_id3 = random.randint(1, 10)
        get_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{random_id}")
        self.assertEqual(get_response.status_code, 200)
        data = get_response.json()

        print(f"GET Request para o usuário com ID {random_id}:")
        print(f"Nome: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Cidade: {data['address']['city']}")
        print("\n")

        new_id = random.randint(11, 30) 
        post_payload = {
            "id": new_id,
            "name": "Luis",
            "email": "Luis@email.com",
            "address": {
                "city": "Guara"
            }
        }
        post_response = requests.post("https://jsonplaceholder.typicode.com/users", json=post_payload)
        self.assertEqual(post_response.status_code, 201)
        post_data = post_response.json()

        print(f"POST Request para criar um novo usuário com ID {new_id}:")
        print(f"Nome: {post_data['name']}")
        print(f"Email: {post_data['email']}")
        print(f"Cidade: {post_data['address']['city']}")
        print("\n")

        put_payload = {
            "name": "Jarvis Stark",
            "email": "jarvisstark@emil.com",
            "address": {
                "city": "Meta City"
            }
        }
        put_response = requests.put(f"https://jsonplaceholder.typicode.com/users/{random_id2}", json=put_payload)
        self.assertEqual(put_response.status_code, 200)
        put_data = put_response.json()

        print(f"PUT Request para atualizar o usuário com ID {random_id2}:")
        print(f"Nome: {put_data['name']}")
        print(f"Email: {put_data['email']}")
        print(f"Cidade: {put_data['address']['city']}")
        print("\n")

        delete_response = requests.delete(f"https://jsonplaceholder.typicode.com/users/{random_id3}")
        self.assertEqual(delete_response.status_code, 200)

        print(f"DELETE Request para excluir o usuário com ID {random_id3}")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(APITestSuite)

    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(suite)
