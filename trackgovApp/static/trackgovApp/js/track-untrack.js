/* eslint-disable no-unused-vars */

document.addEventListener("DOMContentLoaded", init, false); // Initialise the DOM Environment

var tracking_table_body = document.getElementById("tracking-table-body");

var check_box_track =  document.getElementsByClassName("switch-input-custom");
var track_label =  document.getElementsByClassName("track-untrack-custom");

function init() {

    for (var i=0; i<check_box_track.length; i++) {
        check_box_track[i].index = i;   // Game changer

        check_box_track[i].onclick = function(e) {
            if (e.target.checked == true) {
                console.log('Tracking :...' + track_label[e.target.index].dataset.onLabel + ' and with bill_id: ' + e.target.id.substring(6))
    
                var xhttp = new XMLHttpRequest();
                xhttp.onreadystatechange = function () {
                    if (this.readyState == 4 && this.status == 200) {
                        // console.log(this.responseText);
                        tracking_table_body.innerHTML = this.responseText
                    }
                };
                xhttp.open("GET", "http://127.0.0.1:8000/trackbillspreferences/?bill_id=" + e.target.id.substring(6) + "&option=" + track_label[e.target.index].dataset.onLabel, true);
                xhttp.send();
                
                // Confirm Script ran successfully
                console.log('Script ran successfully!!!')
            }
    
            else if (e.target.checked != true) {
                console.log('Not Tracking :...' + track_label[e.target.index].dataset.offLabel + ' and with bill_id: ' + e.target.id.substring(6))
    
                var xhttp = new XMLHttpRequest();
                xhttp.onreadystatechange = function () {
                    if (this.readyState == 4 && this.status == 200) {
                        // console.log(this.responseText);
                        tracking_table_body.innerHTML = this.responseText
                    }
                };
                xhttp.open("GET", "http://127.0.0.1:8000/trackbillspreferences/?bill_id=" + e.target.id.substring(6) + "&option=" + track_label[e.target.index].dataset.offLabel, true);
                xhttp.send();

                // Confirm Script ran successfully
                console.log('Script ran successfully!!!')
            }
    
            else {}
        }

    }

}



    

