date = document.querySelector(".date");
day = document.querySelector(".day");
time = document.querySelector(".time");

let d = new Date();
date.innerText += ' '+( d.getDate() + '/' + parseInt(d.getMonth() + 1) + '/' + d.getFullYear() );

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
day.innerText += ' ' + days[d.getDay()] ;

if(d.getHours() < 12){
    amorpm = 'AM';
    hours = d.getHours();
}
else if(d.getHours() == 12){
    amorpm = 'PM';
    hours = d.getHours();
}
else{
    amorpm = 'PM';
    hours = parseInt(d.getHours() - 12);
}

if(d.getMinutes() < 10)
    mins = '0'+d.getMinutes();
else
    mins = d.getMinutes();
time.innerText += ' '+( hours + ':' + mins + ' ' + amorpm );
