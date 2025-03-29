from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Mapeamento das perguntas frequentes
faq = {
    "preço": "O preço do produto é R$ 499,00.",
    "características": "O produto possui uma tela de 6,5 polegadas, processador Snapdragon 888 e 128GB de armazenamento.",
    "garantia": "Sim, o produto vem com garantia de 1 ano.",
    "compra": "Você pode comprar diretamente no nosso site. Posso enviar o link para você?",
    "pagamento": "Aceitamos cartões de crédito, débito e pagamentos via PayPal."
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message').lower()  # Obter a mensagem do usuário e converter para minúsculas
    response = "Desculpe, não entendi sua pergunta."

    # Verificar se a pergunta está no FAQ
    for question, answer in faq.items():
        if question in user_input:
            response = answer
            break
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
