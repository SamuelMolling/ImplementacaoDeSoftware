$(document).ready(function () {
    //Button for consult vehcicles
    $('#btn_consult_vehcicles').click(function () {
        $.ajax({
            url: '/consult',
            type: 'GET',
            success: function (data) {
                $('#btn_consult_vehcicles_by_model').html(data);
            }})
    });
    // Button for submit this consult
    // $('#search_submit').click(function () {
    //     var selectval = $('#parameter_type').val();
    //     var value = $('#search_text').val();
    //     $.get('/getVehicles',
    //     {
    //         parameter_type: selectval,
    //         parameter_value: value
    //     }, function(data){
    //         alert(data);
    //     });
    // })

    // $('#search_submit').click(function () {
    //     var selectval = $('#parameter_type').val();
    //     var value = $('#search_text').val();
    //     $.ajax({
    //         url: '/getVehicles',
    //         type: 'GET',
    //         data: {
    //             parameter_type: selectval,
    //             parameter_value: value
    //         },
    //         success: function (data) {
    //            alert(data);
    //         }});
    // })

});