function initializeWebSocket(url, elementId) {
    const element = document.getElementById(elementId);
    const socket = new WebSocket(url);

    socket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        if (data.counter !== undefined) {
            element.innerText = 'Counter: ' + data.counter;
        }
    };
}
