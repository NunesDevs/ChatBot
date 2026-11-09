import unittest
from app import create_app


class ChatAppTests(unittest.TestCase):
    def setUp(self):
        self.client = create_app().test_client()

    def test_valid_message_and_no_store_headers(self):
        response = self.client.post('/chat', json={'message': 'Qual o PRECO?'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('499,00', response.json['response'])
        self.assertEqual(response.headers['Cache-Control'], 'no-store')
        self.assertNotIn('Access-Control-Allow-Origin', response.headers)

    def test_invalid_payloads_return_consistent_json(self):
        for payload in (None, [], 'text', {}, {'message': None}, {'message': 3}, {'message': ' '}, {'message': 'a' * 501}):
            response = self.client.post('/chat', data='null', content_type='application/json') if payload is None else self.client.post('/chat', json=payload)
            self.assertEqual(response.status_code, 400)
            self.assertIsInstance(response.json['error'], str)
        self.assertEqual(self.client.post('/chat', data='{', content_type='application/json').status_code, 400)
        self.assertEqual(self.client.post('/chat', data='message=preco').status_code, 415)
        self.assertEqual(self.client.post('/chat', data='x' * 4097, content_type='application/json').status_code, 413)


if __name__ == '__main__':
    unittest.main()
