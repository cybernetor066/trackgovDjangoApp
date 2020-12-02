/* eslint-disable no-unused-vars */

document.addEventListener("DOMContentLoaded", init, false); // Initialise the DOM Environment
	
function init() {
    document.addEventListener("click", selectAll, false);
}
// Function to remove warning after 6secs
function selectAll() {
    // document.innerHTML(alert("Hello Cyber!!"));
    var check_box = document.getElementById("check_all");
    var check_box_effect =  document.getElementsByClassName("select-all-custom");
    if (check_box.checked == true) {
        // check_box.innerHTML(alert("Hello Cyber!!"));
        check_box_effect.forEach(element => {
            element.setAttribute('checked', 'checked');
            // element.checked = true;
        });
    }
    else {
        check_box_effect.forEach(element => {
            element.removeAttribute('checked')
            // element.checked = false;
        });
    }
}
