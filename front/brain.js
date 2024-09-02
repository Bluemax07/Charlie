$(document).ready(function() {
    var siriWave = new SiriWave({
        container: document.getElementById("siri"),
        width: 850,
        height: 200,
        style: "ios9",
        amplitude: "1",
        autostart: true
    });

    $("#mic").click(function() {
        $("#anim").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.all(); // Start listening for voice input
    });

    function ShortKey(e) {
        if (e.key === "j" && e.metaKey) {
            $("#anim").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.all(); // Start listening for voice input
        }
    }
    document.addEventListener('keyup', ShortKey, false);
 
    function pl_assit(message) {

        if (message != "") {

            $("#anim").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.all(message);
            $("#chatbox").val("")
            $("#mic").attr('hidden', false);
            $("#send").attr('hidden', true);

        }

    }

    function change(message) {
        if (message.length == 0) {
            $("#mic").attr('hidden', false);
            $("#send").attr('hidden', true);
        }
        else {
            $("#mic").attr('hidden', true);
            $("#send").attr('hidden', false);
        }
    }

    $("#chatbox").keyup(function () {

        let message = $("#chatbox").val();
        change(message)
    
    });

    $("#send").click(function () {
    
        let message = $("#chatbox").val()
        pl_assit(message)
    
    });
    $("#chatbox").keypress(function (e) {
        key = e.which;
        if (key == 13) {
            let message = $("#chatbox").val()
            pl_assit(message)
        }
    });




});