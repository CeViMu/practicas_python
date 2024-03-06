function getDaysInMonth(month, year) {
    var date = new Date(year, month, 1);
    var days = [];

    var lastDay = new Date(year, month, 0).getDate();
    for (i = date.getDay() - 1; i >= 0; i--) {
        days.push(new Date(year, month - 1, lastDay - i));
    }
    while (date.getMonth() === month) {
        days.push(new Date(date));
        date.setDate(date.getDate() + 1);
    }

    var date3 = new Date(year, month + 1, 1);
    for (i = days[days.length - 1].getDay(); i != 6; i++) {
        days.push(new Date(date3));
        date3.setDate(date3.getDate() + 1);
    }

    for (i = days.length; i != 42; i++) {
        days.push(new Date(date3));
        date3.setDate(date3.getDate() + 1);
        
    }
   
    return days;
   

}

getDaysInMonth(10,2023)
 