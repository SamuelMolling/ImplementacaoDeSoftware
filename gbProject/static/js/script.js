$(document).ready(function () {
    $('#btn_consult_vehcicles').click(function () {
        // $(this).load('/consult');
        $.ajax({
            url: '/consult',
            type: 'GET',
            success: function (data) {
                $('#btn_consult_vehcicles_by_model').html(data);
            }})
    });
    $('#search').click(function () {
        $(this).load('/getVehicles');
    });



    // $('#btn_make_lease').click(function () {
    //     $(this).load('/makelease');
    // });
});