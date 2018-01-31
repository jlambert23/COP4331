var url = window.location.href;
var ext = ".py"
var user;

function login(username, password) {
    
    if (username === "" || password === "") {
        hideOrShow("warningBox", true);
        return;
    }
		
    console.log(username + "\n" + password);   
       
    var jsonPayload = '{"username" : "' + username + '", "password" : "' + hashPassword(password) + '"}';   
    
	// Configure AJAX.
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "API/login" + ext, false);
    xhr.setRequestHeader("Content-type", "application/json; charset=UTF-8");

	// Send json payload and update page.
	try {
        xhr.send(jsonPayload);
        var jsonReceive = JSON.parse( xhr.responseText );
        console.log(jsonReceive);
       
        // Error checking.
        if ( jsonReceive.hasOwnProperty('error') ) {
            hideOrShow("warningBox", true);
            return;
        }
        user = jsonReceive[0];
		
        hideOrShow("loginForm", false);
        presentTable(jsonReceive);
    }
    catch(err) {
        // Need some sort of popup window here.
        console.log(err);
    }
}

// Forge a set of cryptography tools in javascript for webapps and such.
// https://github.com/digitalbazaar/forge#sha256
function hashPassword(password) {
    var hash = forge.md.sha256.create();

    // Stores user password inside hash.
    hash.update(password);

    // Update password to hashed hex.
    password = hash.digest().toHex();

    return password;

}

function hideOrShow(elementId, showState) {
    var vis = "visible";
    var dis = "block";
    if (!showState) {
        vis = "hidden";
        dis = "none";
    }
    document.getElementById(elementId).style.visibility = vis;
    document.getElementById(elementId).style.display = dis;
}

function addBtn(){
	var firstname = document.getElementById("firstNameBox").value;
    var lastname = document.getElementById("lastNameBox").value;
    var email = document.getElementById("emailBox").value;
    var phone = document.getElementById("phoneBox").value;
        
    var jsonPayload = '{"userid" : '+ user[3] +', "firstname" : "' + firstname + '", "lastname" : "' + lastname + '", "email" : "' + email + '", "phone" : "' + phone + '"}';
    console.log(jsonPayload);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url + "API/add" + ext, false);
    xhr.setRequestHeader("Content-type", "application/json; charset=UTF-8");

	try {
        xhr.send(jsonPayload);
        var jsonReceive = JSON.parse( xhr.responseText );
        console.log(jsonReceive);
        // Error checking.
        if ( jsonReceive.hasOwnProperty('error') ) {
            hideOrShow("warningBox", true);
            return;
        }
        
        presentTable(jsonReceive);
    }
    catch(err) {
        // Need some sort of popup window here.
        console.log(err);
    }
}

function presentTable(jsonObject) {
    hideOrShow("queryForm", true);
    
    var count = Object.keys(jsonObject).length;
    
    var txt ="";
    txt += "<table class='table table-striped' id='myTable'>";
    txt += "<thead>";
    txt += "<tr>";
    txt += "<th>Firstname</th>";
    txt += "<th>Lastname</th>";
    txt += "<th>Email</th>";
    txt += "<th>Phone Number</th>";
    txt += "</thead>";
    txt += "</tr>";
    //txt += "</table>";
        
    for (i = 1; i < count; i++){ 
        txt += "<tr>";
        txt += "<td>" + jsonObject[i].firstname + "</td>";
        txt += "<td>" + jsonObject[i].lastname + "</td>";
        txt += "<td>" + jsonObject[i].email + "</td>";
        txt += "<td>" + jsonObject[i].phone + "</td>";
        txt += "<td>" + "<button id='rowBtn' style='margin-left:2%;' type='button' class='btn btn-danger'>Delete</button>" + "</td>";
        /*for (i = 0; i < count; i++) {
            	txt += "<td>" + jsonObject[i]+ "</td>";
                
        } */
        txt += "</tr>"
    }
    txt += "</table>"
    
    
    document.getElementById("view").innerHTML = txt;    
}
