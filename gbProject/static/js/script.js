$(document).ready(function () {
    

    //Button for consult vehicles
    $('#btn_consult_vehcicles').click(function () {
        $.ajax({
            url: '/consultVehcicle',
            type: 'GET',
            success: function (data) {
                $('#btn_consult_vehcicles_by_model').html(data);
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
        }   })
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
                            var days = $('#numberOfDays').val()
                            var vehicle_id = $("input[name='vehicle']:checked").val();
                            if(!vehicle_id){
                                alert("Select a vehicle option");
                            } else {
                                if ((days == '')){
                                    alert("Please enter a day value");
                                }else{
                                    args = {
                                        client_name: client_name,
                                        origin_city: origin_city,
                                        vehicles: vehicle_id,
                                        days: days,
                                    };
                                    $.post('/makeLocation', args, function(data) {
                                        $('#result').html(data);
                                    });
                                }
                            }
                        })
                    });
                })
            }})
    });
    
    //Button for make return
    $('#btn_make_return').click(function () {
        $.ajax({
            url: '/makeReturn',
            type: 'GET',
            success: function (data) {
                $('#btn_consult_return').html(data);
                $("#names_button").load("/getName");
                $("#origin_city_button").load("/getOriginCity");
                $("#next_submit").click(function () {
                    var client_name = $('#names_button').val();
                    var kmDriven = $('#kmDriven').val()
                    if ((kmDriven == '')){
                        alert("Please enter a kilometer value");
                    }else{
                        $.get('/makeReturnLease',
                        {
                            kmDriven: kmDriven,
                            client_name: client_name
                        }, function(data) {
                            $('#result').html(data);
                            $('#btn_return').click(function () {
                                var destination_city = $('#origin_city_button').val();
                                args = {
                                    kmDriven: kmDriven,
                                    client_name: client_name,
                                    destination_city: destination_city,
                                };
                                $.post('/makeReturnLease', args, function(data) {
                                    $('#result').html(data);
                                });
                            }
                        )
                    });
                }
            })
        }})
    });

    //Button for consult leases
    $('#btn_consult_locations').click(function () {
        $.ajax({
            url: '/consultLeases',
            type: 'GET',
            success: function (data) {
                $('#btn_consult_locations_html').html(data);
                $('#search_submit').click( function() {
                    var selectval = $('#parameter_type').val();
                    var selectval2 = $('#search_text').val();
                    if ($('#search_text').val().trim() == ''){
                        alert("Please enter a value");
                    }else{
                        $.get('/consultLeasesByType',
                        {
                            parameter_type: selectval,
                            parameter_value: selectval2
                        }, function(data) {
                            $('#result').html(data);    
                            $('#btnExport').click(function () {
                                var gfm = turndownPluginGfm.gfm
                                var turndownService = new TurndownService()
                                turndownService.use(gfm)
                                var markdown = turndownService.turndown($('#table_export').html())
                                var blob = new Blob([markdown], { type: "text/markdown; charset=utf-8" });
                                saveAs(blob, "table.md");
                            })
                        });
                    }
                }
            )}
        })
    });
    
    //Button for resume
    $('#btn_resume').click(function () {
        $.ajax({
            url: '/resume',
            type: 'GET',
            success: function (data) {
                $('#result').html(data);
            }})
    });
});

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