











// Add on click function to footer links extra to display an error message
$(document).ready(function () {

    let errorMessage = $('.error-msg-links')[0];
    let socialMediaIcons = $('.social-media-symbols').children('li');

    socialMediaIcons.click(function () {
        console.log('click');
        errorMessage.style.display = "block";
        socialMediaIcons.css('pointer-events', 'none');

        window.setTimeout(() => {
            errorMessage.style.opacity = "1";
        }, 100)
        window.setTimeout(() => {
            errorMessage.style.opacity = "0";
        }, 5100)
        window.setTimeout(() => {
            errorMessage.style.display = "none";
            socialMediaIcons.css('pointer-events', 'all');
        }, 6100)
    })
})
