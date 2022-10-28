$(document).ready(function () {
    $('#btn_consult_vehcicles').click(function () {
        $(this).load('/consult');
    });

    $('#btn_make_lease').click(function () {
        $(this).load('/makelease');
    });
});