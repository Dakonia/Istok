document.addEventListener('DOMContentLoaded', function () {
    const otherUserElement = document.querySelector('#other-user');
    if (otherUserElement) {
        const otherUser = otherUserElement.textContent.trim();

        const chatSocket = new WebSocket(
            'ws://' + window.location.host + '/ws/chat/' + otherUser + '/'
        );

        chatSocket.onopen = function (event) {
            console.log('WebSocket connection opened:', event);
        };

        chatSocket.onmessage = function (event) {
            const data = JSON.parse(event.data);
            console.log('Received data from server:', data);

            const sender = data.username;
            const message = data.message;

            const messageElement = document.createElement('p');
            messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;

            const chatMessagesContainer = document.getElementById('chat-messages');
            chatMessagesContainer.appendChild(messageElement);
            chatMessagesContainer.scrollTop = chatMessagesContainer.scrollHeight;
        };

        chatSocket.onclose = function (event) {
            console.log('WebSocket connection closed:', event);
        };

        document.querySelector('#send-button').onclick = function () {
            const messageInputDom = document.querySelector('#message-input');
            const message = messageInputDom.value;

            chatSocket.send(JSON.stringify({
                'message': message,
                'username': "{{ request.user.username }}"
            }));
            messageInputDom.value = '';
        };
    } else {
        console.error('Element with id "other-user" not found.');
    }
});
