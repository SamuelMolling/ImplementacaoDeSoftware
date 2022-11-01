$(document).ready(function () {
    //Button for consult vehicles
    $('#btn_consult_vehicles').click(function () {
        $.ajax({
            url: '/consultVehcicle',
            type: 'GET',
            success: function (data) {
                $('#btn_consult_vehicles_by_model').html(data);
                $('#search_submit').click( function() {
                    var selectval = $('#parameter_type').val();
                    var selectval2 = $('#search_text').val();
                    if ($('#search_text').val().trim() == ''){
                        alert("Please enter a value");
                    }else{
                        $.get('/getVehicles',
                        {
                            parameter_type: selectval,
                            parameter_value: selectval2
                        }, function(data) {
                            $('#result').html(data);
                        });
                    }
                })
            }})
    });

    //Button for make lease
    $('#btn_make_lease').click(function () {
        $.ajax({
            url: '/makeLease',
            type: 'GET',
            success: function (data) {
                $('#btn_consult_lease').html(data);
                $("#names_button").load("/getName");
                $("#origin_city_button").load("/getOriginCity");
                $("#next_submit").click(function () {
                    var client_name = $('#names_button').val();
                    var origin_city = $('#origin_city_button').val();
                    $.get('/makeLocation',
                    {
                        client_name: client_name,
                        origin_city: origin_city
                    }, function(data) {
                        $('#result').html(data);
                        $('#btn_confirm').click(function () {
                            var client_name = $('#names_button').val();
                            var origin_city = $('#origin_city_button').val();
                            var vehicles = $('#vehicle_option').val()
                            var days = $('#numberOfDays').val()
                            $.post('/makeLocation'),
                            {
                                client_name: client_name,
                                origin_city: origin_city,
                                vehicles: vehicles,
                                days: days
                            }, function(data) {
                                $('#result').html(data);
                            }
                        })
                    });
                })

            }})
   });
    
    //Button for make return
    $('#btn_make_return').click(function () {
        $.ajax({
            url: '/makeLease',
            type: 'GET',
            success: function (data) {
                $('#btn_consult_return').html(data);
            }})
    });
    //Button for consult leases
    $('#btn_consult_locations').click(function () {
        $.ajax({
            url: '/consultLeases',
            type: 'GET',
            success: function (data) {
                $('#btn_consult_locations_html').html(data);
            }})
    });
    //Button for resume
    $('#btn_resume').click(function () {
        $.ajax({
            url: '/resume',
            type: 'GET',
            success: function (data) {
                $('#btn_resume_html').html(data);
            }})
    });
    })

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