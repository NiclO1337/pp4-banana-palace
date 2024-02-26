// Add on click function to footer links extra to display an error message
$(document).ready(function () {
    let errorMessage = $('.error-msg-links')[0];
    $('.footer-links-extra').children('li').click(function () {
        errorMessage.style.display = "block";
        window.setTimeout(() => {
            errorMessage.style.opacity = "1";
        }, 100)
        window.setTimeout(() => {
            errorMessage.style.opacity = "0";
        }, 5100)
        window.setTimeout(() => {
            errorMessage.style.display = "none";
        }, 6100)
    })
})

$(document).ready(function() {
    $('#header-container')[0].style.height = "4rem";

    $('main.flex-grow-1')[0].style.marginTop = "20vh";

    $('.navbar-brand')[0].style.display = "block";
    $('#main-logo')[0].style.display = "none";

    $('#navbarNav')[0].classList.remove('justify-content-center');
    $('#navbarNav')[0].classList.add('justify-content-end');
    $('#navbarNav')[0].classList.remove('mt-3');

    $('#header-address-nav')[0].classList.remove('d-sm-block')
    $('#header-phone-nav')[0].classList.remove('d-sm-block')
    $('#header-address')[0].classList.remove('d-block')
    $('#header-phone')[0].classList.remove('d-block')
})





