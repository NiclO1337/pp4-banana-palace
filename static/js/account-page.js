// Makes it more clear that shaking symbol is supposed to be clicked
// Adds opacity to make "Click me!" text visible and change animation
$(document).ready(function() {
    setInterval(function() {

        $('#click-me')[0].style.opacity = '1';
        $('#click-me').parent('a').parent('p').addClass("fa-beat-fade");
        $('#click-me').siblings('i').removeClass("fa-shake");

    }, 10000);
});

