console.log("Hello World!")



// When the user scrolls down 80px from the top of the document,
// resize the navbar's padding and the logo's font size
window.onscroll = function () {
    scrollFunction();
};

function scrollFunction() {
    if (
      document.body.scrollTop > 80 ||
      document.documentElement.scrollTop > 80
    ) {

        $("div.container-fluid")[0].style.padding =
            "0";
    } else {
        $("div.container-fluid")[0].style.padding =
            "80px 0";
    }
}