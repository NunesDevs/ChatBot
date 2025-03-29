function sendMessage() {
    var userInput = document.getElementById("user_input").value;
    if (!userInput) return;

    var chatbox = document.getElementById("chatbox");

    // Exibe a pergunta do usuário no chatbox
    chatbox.innerHTML += "<div><strong>Você:</strong> " + userInput + "</div>";

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
        chatbox.innerHTML += "<div><strong>Bot:</strong> " + data.response + "</div>";

        // Rola para o final do chat
        chatbox.scrollTop = chatbox.scrollHeight;
    });
}
