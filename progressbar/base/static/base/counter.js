function initializeWebSocket(url, elementId) {
  const element = document.getElementById(elementId);
  const socket = new WebSocket(url);
  
  socket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    if (data.counter !== undefined) {
      var msg = 'Counter: ' + data.counter;
      msg += ' Total:' + data.total
      element.innerText = msg;
    }
  };
}
