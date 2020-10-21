//Skripta funkcionalnost sata
setInterval(syncClock, 1000);



var hour = document.querySelector('[data-hour]');
var minute = document.querySelector('[data-minute]');
var second = document.querySelector('[data-second]');

function syncClock(){
    var currentTime = new Date();
    var seconds = currentTime.getSeconds() / 60;
    var minutes = (seconds + currentTime.getMinutes()) / 60;
    var hours = (minutes + currentTime.getHours()) / 12;
    rotateHands(hour, hours);
    rotateHands(minute, minutes);
    rotateHands(second, seconds);
}

function rotateHands(hand, rotation){
    hand.style.setProperty('--rotation', rotation * 360);

}



syncClock();