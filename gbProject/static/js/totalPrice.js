function TotalPrice(days, km_driven, price_by_day, price_by_km) {
    var days = days
    var km_driven = km_driven
    var price_by_day = daily_value
    var price_by_km = km_value
    var total_price = (days * price_by_day) + (km_driven * price_by_km)
    return total_price
}