console.log("Hello World!")


// When the user scrolls down 80px from the top of the document,
// resize the navbar's padding and the logo's font size
window.onscroll = function () {
    scrollFunction();
};

function scrollFunction() {
    if (
        document.body.scrollTop > 1 || document.documentElement.scrollTop > 1
    ) {
        $('#header-container')[0].style.height = "4rem";

        $('main.container')[0].style.marginTop = "15rem";

        $('.navbar-brand')[0].style.display = "block";
        $('#main-logo')[0].style.display = "none";

        $('#navbarNav')[0].classList.remove('justify-content-center');
        $('#navbarNav')[0].classList.add('justify-content-end');
        $('#navbarNav')[0].classList.remove('mb-auto');
    } else {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
        $('#header-container')[0].style.height = "8rem";

        $('main.container')[0].style.marginTop = "6rem";

        $('.navbar-brand')[0].style.display = "none";
        $('#main-logo')[0].style.display = "block";

        $('#navbarNav')[0].classList.remove('justify-content-end');
        $('#navbarNav')[0].classList.add('justify-content-center');
        $('#navbarNav')[0].classList.add('mb-auto');
    }
}