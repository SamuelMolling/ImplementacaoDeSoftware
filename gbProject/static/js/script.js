$(document).ready(function () {

    function closeButton(button) {
        var divs = document.getElementsByTagName('div')
        for (var i = 0; i < divs.length; i++) {
            if (divs[i].id != button && divs[i].id!='result')
                $(divs[i]).hide()
                $(button).show()
        }
    }

    //Button for consult vehicles
    $('#btn_consult_vehcicles').click(function () {
        closeButton('#btn_consult_vehcicles_by_model')
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
        closeButton('#btn_consult_lease')
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
        closeButton('#btn_consult_return')
        $.ajax({
            url: '/makeReturn',
            type: 'GET',
            success: function (data) {
                $('#btn_consult_return').html(data);
                $("#names_button_return").load("/getName");
                $("#origin_city_button_return").load("/getOriginCity");
                $("#next_submit").click(function () {
                    var client_name = $('#names_button_return').val();
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
                                var destination_city = $('#origin_city_button_return').val();
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
        closeButton('#btn_consult_locations_html')
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