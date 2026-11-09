# Assistente de produto

FAQ demonstrativo com interface web desenhada no Figma, conversa por teclado, perguntas sugeridas e respostas locais sobre preço, características, garantia, compra e pagamento. As informações são demonstrativas; nenhuma compra ou pagamento é realizado.

## Executar

Validado com Python 3.12. Use ambiente isolado e o lock com hashes:

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install --only-binary=:all: --require-hashes -r requirements.lock
.venv\Scripts\python app.py
```

Abra `http://127.0.0.1:5000`. Em Linux/macOS, substitua pelo executável `.venv/bin/python`. O servidor inicia em loopback com debug desativado.

## Recursos e arquitetura

`answers.py` contém o FAQ e busca por palavras/expressões normalizadas, sem diferença de acentos ou maiúsculas. As respostas são determinísticas, sem modelo de IA nem requisições externas. `app.py` expõe a página Jinja e `POST /chat`, validando objeto JSON, tipo de mensagem, conteúdo e tamanho; mensagens aceitam de 1 a 500 caracteres e a requisição tem limite de 4096 bytes.

A interface usa texto DOM, sem interpretar HTML das mensagens. Envio pendente desativa duplicatas; erro/timeout preserva a pergunta para nova tentativa, que reutiliza a linha do usuário. Limpar cancela a requisição e ignora respostas tardias. O histórico fica somente na página, limitado a cem linhas, e desaparece ao recarregar. Fontes são locais sob OFL.

```powershell
.venv\Scripts\python -m unittest discover -s tests -v
node --test tests/chatbot.test.cjs
```

Cinco testes Python verificam normalização, limites e contratos JSON/HTTP. Quatro testes Node verificam texto seguro, envio concorrente, nova tentativa sem duplicação e cancelamento. A passagem Playwright e as capturas ficam registradas na memória técnica.

`requirements.txt` fixa Flask; `requirements.lock` fixa dependências transitivas com hashes dos artefatos oficiais. Licença MIT em `LICENSE`; licenças das fontes em `static/fonts/`. Memória: `docs/ai-context/QUALITY_REFRESH.md`.
