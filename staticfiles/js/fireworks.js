// Fade in elements on fireworks page on timers
$(document).ready(function() {
    setInterval(function() {
        $('h1')[0].style.opacity = "1";
    },1500)
    setInterval(function() {
        $('#name')[0].style.opacity = "1";
    },2500)
    setInterval(function() {
        $('p')[0].style.opacity = "1";
    },4000)
    setInterval(function() {
        $('.account-management>a')[0].style.opacity = "1";
    },6000)
})