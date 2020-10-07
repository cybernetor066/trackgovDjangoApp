// Source code for a customised wall clock in JavaScript.
//Courtesy **Anetor Eguakhide Kunle** (A Software-IT Dev Engineer).
var D = new Date();
var M = new Date();
var d = new Date();
var Y = new Date();
var H = new Date();
var m = new Date();


var lengthDate = d.getDate().toString().length;
var lengthHour = H.getHours().toString().length;
var lengthMin = m.getMinutes().toString().length;


var days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
var months = ["Jan","Feb","March","April","May","June","July","August","September","October","November","December"];
var amHours = [0,1,2,3,4,5,6,7,8,9,10,11];
var pmHours = [12,13,14,15,16,17,18,19,20,21,22,23];


if(amHours.includes(H.getHours())) document.getElementById("AM-PM").innerHTML = "AM";
if(pmHours.includes(H.getHours())) document.getElementById("AM-PM").innerHTML = "PM";

document.getElementById("Day").innerHTML = days[D.getDay()];
document.getElementById("Month").innerHTML = months[M.getMonth()];
document.getElementById("date").innerHTML = d.getDate();
document.getElementById("Year").innerHTML = Y.getFullYear();
document.getElementById("Hour").innerHTML = H.getHours();
document.getElementById("Min").innerHTML = m.getMinutes();

if(lengthDate != 2) document.getElementById("date").innerHTML = "0" + d.getDate();
if(lengthHour != 2) document.getElementById("Hour").innerHTML = "0" + H.getHours();
if(lengthMin != 2) document.getElementById("Min").innerHTML = "0" + m.getMinutes();


// Conversion code for 24HR -- 12HR Format.
var twentyFour = [13,14,15,16,17,18,19,20,21,22,23];
var twelve = ['1','2','3','4','5','6','7','8','9','10','11'];
function twelveHourConverter () {
    var zero = "0";
    for(let y=0; y<=twentyFour.length - 1; y++) {
            if(twentyFour[y] == H.getHours()) {
                if(twelve[y].length == 2) {
                    zero = "";
                    return document.getElementById("Hour").innerHTML = zero + twelve[y];
                }
                else return document.getElementById("Hour").innerHTML = zero + twelve[y];    
            }
    }
}
twelveHourConverter();

