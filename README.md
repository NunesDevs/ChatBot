# Chatbot de Produto com Flask

Este projeto cria um chatbot simples que responde perguntas frequentes sobre um produto utilizando Python e Flask. Ele inclui uma interface frontend simples para interação com o usuário.

## Funcionalidades

- Respostas automáticas para perguntas frequentes sobre o produto.
- Interface simples em HTML, CSS e JavaScript.
- Backend utilizando Flask para processar as mensagens e fornecer as respostas.

## Como Rodar o Projeto

1. Clone o repositório:
    ```
    git clone https://github.com/NunesDevs/ChatBot.git
    cd ChatBot
    ```

2. Crie e ative um ambiente virtual:
    ```
    python -m venv venv
    source venv/bin/activate   # No Windows, use venv\Scripts\activate
    ```

3. Instale as dependências:
    ```
    pip install -r requirements.txt
    ```

4. Execute o servidor Flask:
    ```
    pip install --upgrade Flask

    python app.py
    ```

5. Acesse o chatbot no navegador:
    ```
    http://127.0.0.1:5000
    ```

## Tecnologias Usadas

- Flask
- HTML, CSS e JavaScript

## Operação e arquitetura verificadas

Flask em app.py publica a página Jinja e a API; static/js/chatbot.js envia mensagens via fetch. Respostas são determinadas por um dicionário local, sem modelo de IA.

Arquivos principais: `app.py`, `static/js/chatbot.js`, `requirements.txt`.

### Requisitos e execução

Python 3 e Flask; Node.js para o teste do frontend.

```text
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python app.py
node --test tests/chatbot.test.cjs
```



### Testes e estado

O teste Node verifica que mensagens do usuário e respostas do bot são inseridas como texto, incluindo entradas com marcação maliciosa. O backend Flask não foi exercitado.

Estado: projeto de estudo/experimental. Deploy ativo não foi confirmado nesta revisão.

### Limitações conhecidas

- O backend ainda precisa validar formato e tamanho da mensagem.
- Dependências antigas precisam avaliação de compatibilidade antes de atualização.
- Servidor debug destina-se apenas ao desenvolvimento local.

### Licença e manutenção

Nenhum arquivo de licença foi identificado nesta revisão; não foi adicionada uma nova licença. Atualize comandos e limitações quando houver mudança de comportamento.
