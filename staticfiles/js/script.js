// When the user scrolls down 1px from the top of the document,
// change many css settings to change the UI, then back again
// if user scrolls back to top.
window.onscroll = function () {
    scrollFunction();
};

function scrollFunction() {

    if (
        document.body.scrollTop > 1 || document.documentElement.scrollTop > 1
    ) {
        $('#header-container')[0].style.height = "4rem";

        $('main.flex-grow-1')[0].style.marginTop = "20vh";
        $('.soft-cushion')[0].style.height = "1vh";
        $('.soft-cushion')[1].style.height = "1vh";


        $('.navbar-brand')[0].style.display = "block";
        $('#main-logo')[0].style.display = "none";

        $('#navbarNav')[0].classList.remove('justify-content-center');
        $('#navbarNav')[0].classList.add('justify-content-end');
        $('#navbarNav')[0].classList.remove('mt-3');

        $('#header-address-nav')[0].classList.remove('d-sm-block')
        $('#header-phone-nav')[0].classList.remove('d-sm-block')
        $('#header-address')[0].classList.remove('d-block')
        $('#header-phone')[0].classList.remove('d-block')

    } else {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
        $('#header-container')[0].style.height = "8rem";

        $('main.flex-grow-1')[0].style.marginTop = "0";
        $('.soft-cushion')[0].style.height = "8vh";
        $('.soft-cushion')[1].style.height = "8vh";

        $('.navbar-brand')[0].style.display = "none";
        $('#main-logo')[0].style.display = "block";

        $('#navbarNav')[0].classList.remove('justify-content-end');
        $('#navbarNav')[0].classList.add('justify-content-center');
        $('#navbarNav')[0].classList.add('mt-3');


        $('#header-address-nav')[0].classList.add('d-sm-block')
        $('#header-phone-nav')[0].classList.add('d-sm-block')
        $('#header-address')[0].classList.add('d-block')
        $('#header-phone')[0].classList.add('d-block')
    }
}


// Code snippet let items from https://codepen.io/hellomev/pen/LYORMQW

let items = document.querySelectorAll('.carousel .carousel-item')

		items.forEach((el) => {
			const minPerSlide = 4
			let next = el.nextElementSibling
			for (var i=1; i<minPerSlide; i++) {
				if (!next) {
            // wrap carousel by using first child
            next = items[0]
        }
        let cloneChild = next.cloneNode(true)
        el.appendChild(cloneChild.children[0])
        next = next.nextElementSibling
    }
})