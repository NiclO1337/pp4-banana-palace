console.log("Hello World!")



// When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
window.onscroll = function () {
    scrollFunction();
  };

  function scrollFunction() {
    if (
      document.body.scrollTop > 80 ||
      document.documentElement.scrollTop > 80
    ) {
      document.getElementsByClassName("container-fluid")[0].style.padding =
        "30px 10px";
      document.getElementsByClassName("navbar-brand")[0].style.fontSize =
        "25px";
    } else {
      document.getElementsByClassName("container-fluid")[0].style.padding =
        "80px 10px";
      document.getElementsByClassName("navbar-brand")[0].style.fontSize =
        "35px";
    }
  }