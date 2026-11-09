"""FAQ de demonstração; respostas locais determinísticas, sem serviços externos."""
import re
import unicodedata

MAX_MESSAGE_LENGTH = 500
FAQ = {
    'preço': 'O preço do produto é R$ 499,00.',
    'características': 'O produto possui uma tela de 6,5 polegadas, processador Snapdragon 888 e 128GB de armazenamento.',
    'garantia': 'Sim, o produto vem com garantia de 1 ano.',
    'compra': 'Este é um catálogo demonstrativo. Nenhuma compra é realizada aqui.',
    'pagamento': 'Aceitamos cartões de crédito, débito e pagamentos via PayPal.',
}
TERMS = {
    'preço': ('preco', 'precos', 'valor', 'quanto custa'),
    'características': ('caracteristicas', 'caracteristica', 'especificacoes', 'especificacao'),
    'garantia': ('garantia',),
    'compra': ('compra', 'comprar'),
    'pagamento': ('pagamento', 'pagamentos', 'pagar'),
}


def normalize(value):
    decomposed = unicodedata.normalize('NFD', value.casefold())
    return ' '.join(''.join(char for char in decomposed if unicodedata.category(char) != 'Mn').split())


def answer_message(message):
    if not isinstance(message, str):
        raise ValueError('A mensagem deve ser um texto')
    message = message.strip()
    if not 1 <= len(message) <= MAX_MESSAGE_LENGTH:
        raise ValueError('Use uma mensagem de 1 a 500 caracteres')
    normalized = normalize(message)
    for key, terms in TERMS.items():
        if any(re.search(r'\b' + re.escape(term) + r'\b', normalized) for term in terms):
            return FAQ[key]
    return 'Desculpe, não entendi sua pergunta. Posso ajudar com preço, características, garantia, compra e pagamento.'
