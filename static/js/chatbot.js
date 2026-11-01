function appendMessage(chatbox, speaker, message) {
    var row = document.createElement("div");
    var label = document.createElement("strong");
    label.textContent = speaker + ": ";
    row.appendChild(label);
    row.appendChild(document.createTextNode(String(message)));
    chatbox.appendChild(row);
}

function sendMessage() {
    var userInput = document.getElementById("user_input").value;
    if (!userInput) return;

    var chatbox = document.getElementById("chatbox");

    // Exibe a pergunta do usuário no chatbox
    appendMessage(chatbox, "Você", userInput);

    // Limpar o campo de entrada
    document.getElementById("user_input").value = "";

    // Enviar a pergunta para o servidor
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Exibe a resposta do chatbot no chatbox
        appendMessage(chatbox, "Bot", data.response);

        // Rola para o final do chat
        chatbox.scrollTop = chatbox.scrollHeight;
    });
}
