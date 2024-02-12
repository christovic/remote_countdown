var socket = io();
var running = false;

const divid = window.location.pathname == '/' ? "running" : "status"

socket.on('timer_status', function(data) {
    document.getElementById("remote_time").innerText = data.current_time;
        running = data.running
    if (data.running && window.location.pathname == '/') {
        document.getElementById("running").innerText = "Running"
        document.getElementById("running").style.backgroundColor = "Green"
        document.getElementById("toggle_timer").innerText = "Pause"
    } else if (window.location.pathname == '/') {
        document.getElementById("running").innerText = "Stopped"
        document.getElementById("running").style.backgroundColor = "Red"
        document.getElementById("toggle_timer").innerText = "Start"
    }
})

socket.on('time_updated', function(data){
    document.getElementById('time').innerText = data;
})

socket.on('blackout', function(){
    console.log("blackout")
    document.getElementById('remote_time').innerText = "";
})

socket.on('timer_updated', function(data) {
    if (window.location.pathname == '/') {
    document.getElementById("timer_minutes").placeholder = data;
    }
})

socket.on('connect', function(){
    document.getElementById(divid).innerText = "Connected"
    document.getElementById(divid).style.backgroundColor = "Green"
})

socket.on('disconnect', function() {
    document.getElementById(divid).innerText = "Disconnected"
    document.getElementById(divid).style.backgroundColor = "Gray"
})
// if we are the controller, set up keybindings, and clicks
function send_timer() {
        if (document.getElementById("timer_minutes").value != "") {
            socket.emit("set_timer", document.getElementById("timer_minutes").value * 60);
            document.getElementById("timer_minutes").value = "";
        } else {
            if (running == false) {
                socket.emit("set_timer", document.getElementById("timer_minutes").placeholder * 60);
            } else {
                console.log("Starting")
                socket.emit('control', 'start')
            }
        }
}
if (window.location.pathname == '/') {
    document.getElementById("send_timer").addEventListener("click",
        send_timer,
        false
    );

    document.getElementById("timer_minutes").addEventListener("keypress",
    function(event) {
        // If the user presses the "Enter" key on the keyboard
        if (event.key === "Enter") {
        // Cancel the default action, if needed
        event.preventDefault();
        // Trigger the button element with a click
        send_timer()
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
        function() {socket.emit('reset_timer')},
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
}