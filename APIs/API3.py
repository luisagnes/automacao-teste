import requests
import unittest
import random

class APITestSuite(unittest.TestCase):

    def test_user_request(self):
        random_id = random.randint(1, 10)  # Gere um ID aleatório de 1 a 10
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/{random_id}")
        self.assertEqual(response.status_code, 200)
        data = response.json()

        # Imprima os resultados das requisições
        print(f"Request para o usuário com ID {random_id}:")
        print(f"Nome: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Cidade: {data['address']['city']}")
        print("\n")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(APITestSuite)

    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(suite)
