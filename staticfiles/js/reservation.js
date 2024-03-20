$(document).ready(function () {

    // Makes month slider within datepicker smooth
    $(document).on('click', '.ui-datepicker-next', function () {
        $(".ui-datepicker-calendar").hide('slide', { direction: 'left' }, 300).show('slide', { direction: 'right' }, 300);
    });
    $(document).on('click', '.ui-datepicker-prev', function () {
        $(".ui-datepicker-calendar").hide('slide', { direction: 'right' }, 300).show('slide', { direction: 'left' }, 300);
    });

    // Initialize jQuery datepicker
    $('#id_date').datepicker({
    // limit date input between today and 12 months from now
        minDate: 0,
        maxDate: "+12m"
    }).on('change', function() {
    // Submit form when selecting date as well as hide blueprint/tables,
    // and show the loading animation.
        $(this).closest('form').submit();
        $('.table-container')[0].style.opacity = "0";
        $('.spinner')[0].style.display = "block";
    });
});