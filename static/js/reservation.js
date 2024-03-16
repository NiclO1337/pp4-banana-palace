$(document).ready(function () {
    $(document).on('click', '.ui-datepicker-next', function () {
        $(".ui-datepicker-calendar").hide('slide', { direction: 'left' }, 300).show('slide', { direction: 'right' }, 300);
    });

    $(document).on('click', '.ui-datepicker-prev', function () {
        $(".ui-datepicker-calendar").hide('slide', { direction: 'right' }, 300).show('slide', { direction: 'left' }, 300);
    });

    $("#id_date").datepicker({
        onSelect: function (dateText, inst) {
            $(this).closest('form').submit();
        }
    });
});
