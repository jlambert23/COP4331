var url = window.location.href; //"http://18.219.16.244";
var ext = ".py"
var userid;

function login() {
    var userName = document.getElementById("userNameText").value;
    var password = document.getElementById("passwordText").value;

    if (userName === "" || password === "") {
        hideOrShow("warningBox", true);
        return;
    }
    
    // Send json to backend API.
    var jsonPayload = '{"username" : "' + userName + '", "password" : "' + hashPassword(password) + '"}';   
    
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url + "API/login" + ext, false);
    xhr.setRequestHeader("Content-type", "application/json; charset=UTF-8");

	try {
        xhr.send(jsonPayload);
        var jsonReceive = JSON.parse( xhr.responseText );
       
        // Error checking.
        if ( jsonReceive.hasOwnProperty('error') ) {
            hideOrShow("warningBox", true);
            return;
        }
        
        userid = jsonReceive[0];
        console.log(userid)
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
    console.log("gabba" + vis + dis);
    document.getElementById(elementId).style.visibility = vis;
    document.getElementById(elementId).style.display = dis;
}

function addBtn(){
	var firstname = document.getElementById("firstNameBox").value;
    var lastname = document.getElementById("lastNameBox").value;
    var email = document.getElementById("emailBox").value;
    var phone = document.getElementById("phoneBox").value;
        
    var jsonPayload = '{"userid" :'+ userid +', "firstname" : "' + firstname + '", "lastname" : "' + lastname + '", "email" : "' + email + '", "phone" : "' + phone + '"}';
    
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url + "API/add" + ext, false);
    xhr.setRequestHeader("Content-type", "application/json; charset=UTF-8");

	try {
        xhr.send(jsonPayload);
        var jsonReceive = JSON.parse( xhr.responseText );
       
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

function searchBtn(){
	console.log("search"); 
}

function presentTable(jsonObject)
{
    hideOrShow("queryForm", true);
    
    var count = Object.keys(jsonObject).length;
    console.log("Size of json objects " + count);
    
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
    
    console.log(jsonObject);
    
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
    console.log("end of presentTable");
    
}