// Skripta gde se nalaze sve funkcionalnosti sajta, osim sata
var hour = document.querySelector('[data-help-hour]');
var minute = document.querySelector('[data-help-minute]');

function change(){

    document.getElementById("refill-time-change").style.display = "block";
    document.getElementById("done-btn").style.display = "block";
    document.getElementById("change-btn").style.display = "none";
    document.getElementById("refill-time").style.display = "none";

}

function done(){  

    var time = document.getElementById("refill-time-change-text").value;
    validacija(time);

}

function rotateHandsH(help, rotation){
    help.style.setProperty('--rotationH', rotation * 360);

}


// Nastavak glavne skripte
function validacija(time){

    if(time.length != 5 || time[2] != ':'){
        alert("Expected time format: 'hh:mm'");
        return;
    }

    if(isNaN(parseInt(time.substring(0,2))) || isNaN(parseInt(time.substring(3, )))){
        alert("Expected time format: 'hh:mm'");
        return;
    }

    var hours = parseInt(time.substring(0,2));
    var minutes = parseInt(time.substring(3, ))
    var rotationHour = hours / 12;
    var rotationMinute = minutes / 60;

    document.getElementById("refill-time-change").style.display = "none";
    document.getElementById("done-btn").style.display = "none";
    document.getElementById("change-btn").style.display = "block";
    document.getElementById("refill-time").style.display = "block";

    document.getElementById("time").innerHTML = time;
    
    rotateHandsH(hour, rotationHour);
    rotateHandsH(minute, rotationMinute);
    
    sendTime(hours, minutes);
}

// Simulacija komunikacije sa rpi flask aplikacijom, pomocu improvizovane test flask aplikacije
function sendTime(hour, minute){
    var time = {'hour' : hour, 'minute' : minute};
    var url = 'http://172.20.222.232:5000/dajbroj';
    
    $.ajax({
        url: url,
        type: 'GET',
        data: time
    })
    .done(function(data){
        console.log(data);
    });
}


function sendPortionSize(){

    var psize = document.getElementById("size").value;
    var size = {"size" : psize}
    var url = 'http://172.20.222.232:5000/dajporciju';
    
    $.ajax({
        url: url,
        type: 'GET',
        data: size
    })
    .done(function(data){
        console.log(data);
    });

}

function refillNow(){

    var url = 'http://172.20.222.232:5000/sipajodmah';
    
    $.ajax({
        url: url,
        type: 'GET',
    })

}