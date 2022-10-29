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
    // $('#search').click(function () {
    //     $(this).load('/getVehicles');
    // });
    $('#search').click(function () {
        $.ajax({
            url: '/getVehicles',
            type: 'GET',
            success: function (data) {
                $('#result').html(data);
            }})
    });



    // $('#btn_make_lease').click(function () {
    //     $(this).load('/makelease');
    // });
});