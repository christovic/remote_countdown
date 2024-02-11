var socket = io();
var running = false;

socket.on('timer_status', function(data) {
    document.getElementById("remote_time").innerText = data.current_time;
        running = data.running
    if (data.running) {
        document.getElementById("running").innerText = "Running"
        document.getElementById("toggle_timer").innerText = "Pause"
        document.getElementById("running").style.backgroundColor = "Green"
    } else {
        document.getElementById("running").innerText = "Stopped"
        document.getElementById("toggle_timer").innerText = "Start"
        document.getElementById("running").style.backgroundColor = "Red"
    }
})

socket.on('timer_updated', function(data) {
    document.getElementById("timer_minutes").placeholder = data + "m";
})

socket.on('disconnect', function() {
    document.getElementById("running").innerText = "Disconnected"
    document.getElementById("running").style.backgroundColor = "Gray"
})

document.getElementById("send_timer").addEventListener("click",
    function() {socket.emit("set_timer", document.getElementById("timer_minutes").value * 60)},
    false
);
document.getElementById("timer_minutes").addEventListener("keypress",
function(event) {
    // If the user presses the "Enter" key on the keyboard
    if (event.key === "Enter") {
      // Cancel the default action, if needed
      event.preventDefault();
      // Trigger the button element with a click
      if (document.getElementById("timer_minutes").value != "") {
        document.getElementById("send_timer").click();
        document.getElementById("timer_minutes").value = "";
      } else {
        if (running == false) {
            document.getElementById("reset_timer").click();
        } else {
            console.log("Starting")
            socket.emit('control', 'start')
        }
      }
    }
});
document.onkeydown = function(evt) {
    evt = evt || window.event;
    if (evt.keyCode == 32) {
        if (document.getElementById("timer_minutes").value != "") {
            document.getElementById("send_timer").click();
            document.getElementById("timer_minutes").value = "";
            socket.emit('control', 'start')
        } else {
            toggleTimer();
        }
    } else if (evt.keyCode == 82) {
        socket.emit('control', 'pause')
        socket.emit('control', 'pause')
    }
}
document.getElementById("toggle_timer").addEventListener("click",
    function() {
        toggleTimer()
    },
    false
);
document.getElementById("reset_timer").addEventListener("click",
    function() {socket.emit('control', 'pause')},
    false
);
function toggleTimer() {
    if (running) {
        socket.emit('control', 'pause')
    } else {
        socket.emit('control', 'start')
    }
}

document.getElementById('timer_minutes').onblur = function (event) { var blurEl = this; setTimeout(function() {blurEl.focus()},10) };
window.onload = function() {
    var input = document.getElementById("timer_minutes").focus();
  }