var JUGGERNAUT_SERVER = document.location.hostname,
    JUGGERNAUT_PORT   = document.location.port || 80;

var log = function(data){
    console.log(data);
};

var jug = new Juggernaut({
    secure: ('https:' == document.location.protocol),
    host: JUGGERNAUT_SERVER,
    port: JUGGERNAUT_PORT
});

jug.on("connect", function(){ log("Connected") });
jug.on("disconnect", function(){ log("Disconnected") });
jug.on("reconnect", function(){ log("Reconnecting") });

log("Subscribing to channel1");

var reload = false,
    id;

var wait_or_reload = function() {
    window.location.reload();
}

jug.subscribe("channel1", function(data){
    log("Got data: " + data);
    if (reload) {
        if (id) {
            clearTimeout(id);
        }
    }
    else {
        reload = true;
    }
    id = setTimeout(wait_or_reload, 1000);
});
