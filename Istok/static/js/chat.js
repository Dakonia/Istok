document.addEventListener("DOMContentLoaded", function() {
    const chat = document.getElementById("chat");
    const openChatBtn = document.getElementById("open-chat-btn");
    const chatSendBtn = document.getElementById("chat-send");
    const chatInput = document.getElementById("chat-input");
    const outputBlock = document.getElementById("output-block");

    openChatBtn.addEventListener("click", function() {
        chat.style.display = "block";
        openChatBtn.style.display = "none";
    });

    document.addEventListener("click", function(event) {
        if (!chat.contains(event.target) && event.target !== openChatBtn) {
            chat.style.display = "none";
            openChatBtn.style.display = "block";
        }
    });

    chatSendBtn.addEventListener("click", function() {
        const message = chatInput.value.trim();
        if (message) {
            const messageElement = document.createElement("div");
            messageElement.textContent = message;
            messageElement.classList.add("message");
            outputBlock.prepend(messageElement); 
            chatInput.value = ""; 
            outputBlock.scrollTop = 0; 
        }
    });
});
