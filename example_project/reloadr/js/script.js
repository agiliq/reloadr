<script src="application.js" type="text/javascript" charset="utf-8"></script>
<script type="text/javascript" charset="utf-8">
    var logElement = document.getElementById("log");
    logElement.value = "";
    var log = function(data){
        logElement.value += (data + "\n");
    };

    var jug = new Juggernaut({
        secure: ('https:' == document.location.protocol),
        host: document.location.hostname,
        port: document.location.port || 80
    });

    jug.on("connect", function(){ log("Connected") });
    jug.on("disconnect", function(){ log("Disconnected") });
    jug.on("reconnect", function(){ log("Reconnecting") });

    log("Subscribing to channel1");

    jug.subscribe("channel1", function(data){
        log("Got data: " + data);
    });
</script>
