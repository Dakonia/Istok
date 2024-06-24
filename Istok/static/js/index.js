    const openChatBtn = document.getElementById('openChatBtn');
    const modal = document.getElementById('chatModal');
    const closeModal = document.getElementsByClassName('close')[0];
    const chatContainer = document.getElementById('chat-container');

    openChatBtn.onclick = function() {
        fetch("{% url 'chat_room' username=request.user.username %}")
            .then(response => response.text())
            .then(html => {
                chatContainer.innerHTML = html;
                modal.style.display = "block";
            });
    }

    closeModal.onclick = function() {
        modal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }