// Add on click function to footer social media icons
// to display an error message about missing links
$(document).ready(function () {

    let errorMessage = $('.error-msg-links')[0];
    let socialMediaIcons = $('.social-media-symbols li');

    socialMediaIcons.on('click', socialMediaIcons, function () {
        errorMessage.style.display = "block";
        socialMediaIcons.css('pointer-events', 'none');
        socialMediaIcons.css('color', 'var(--color-tertiary-light)');

        window.setTimeout(() => {
            errorMessage.style.opacity = "1";
        }, 100)
        window.setTimeout(() => {
            errorMessage.style.opacity = "0";
        }, 5100)
        window.setTimeout(() => {
            errorMessage.style.display = "none";
            socialMediaIcons.css('pointer-events', 'all');
            socialMediaIcons.css('color', 'var(--color-primary-bg');
        }, 6100)
    })
})
