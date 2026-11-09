import unittest
from answers import FAQ, answer_message


class AnswerTests(unittest.TestCase):
    def test_all_topics_and_normalized_search(self):
        for message, topic in [(' QUAL É O PRECO? ', 'preço'), ('Quais as ESPECIFICAÇÕES?', 'características'), ('Existe GARANTIA?', 'garantia'), ('Quero comprar', 'compra'), ('Como posso pagar?', 'pagamento')]:
            self.assertEqual(answer_message(message), FAQ[topic])
        self.assertEqual(answer_message('Qual o prec\u0327o?'), FAQ['preço'])

    def test_substrings_do_not_match_unrelated_words(self):
        self.assertIn('não entendi', answer_message('Estou despreocupado'))
        self.assertIn('não entendi', answer_message('<img src=x onerror=alert(1)>'))

    def test_message_types_and_size_are_validated(self):
        for message in (None, [], {}, 5, True, '', '   ', 'a' * 501):
            with self.assertRaises(ValueError):
                answer_message(message)
        self.assertIsInstance(answer_message('a' * 500), str)


if __name__ == '__main__':
    unittest.main()
