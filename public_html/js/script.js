var url = window.location.href; //"http://18.219.16.244";
var ext = ".py"
var userId = null;

function login() {
    var userName = document.getElementById("userNameText").value;
    var password = document.getElementById("passwordText").value;

    if (userName === "" || password == "") {
        hideOrShow("warningBox", true);
        return;
    }

    //hideOrShow("successBox", true);
    // bogus stuff
    presentTable();
    // bogus stuff

    // Send json to backend API.
    var jsonPayload = '{"userName" : "' + userName + '", "password" : "' + hashPassword(password) + '"}';
    var jsonReceive = sendJSON(jsonPayload, url + "API/Login" + ext);
    
    /* presentTable(sendJSON('{"id": "2"}', url + "API/QueryContacts"+ext)); */

    //hideOrShow("loginForm", false);
    console.log(jsonRecieve);
    if (jsonReceive.id)
        console.log("id json id object");
    else if (jsonRecieve.error)
        return;
    
    userId = jsonReceive.id;
    userId = userId[0];

    console.log(typeof userId);

    if (userId < 1 || userId === null){
        alert("User doesn't exist");
        //hideOrShow("loginForm", true);
        return;
    } else {
        hideOrShow("loginForm", false);
        hideOrShow("successBox", true);
    }
    
    //presentTable();
}

function sendJSON(jsonPayload, pyScript) {
    // Configure AJAX
    var xhr = new XMLHttpRequest();
    xhr.open("POST", pyScript);
    xhr.setRequestHeader("Content-type", "application/json; charset=UTF-8");

    // Event handler to asynchronously retrieve response.
	xhr.onreadystatechange = function() {
		if (xhr.readyState == 4 && xhr.status == 200) {
            console.log(xhr.responseText);

            try {
                return JSON.parse(xhr.responseText);
            }
            catch (err) {
                console.log(err + "ERROR XML/JSON");
                return;
            }
		}
	}

    xhr.send(jsonPayload);
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
	console.log("add");
}

function searchBtn(){
	console.log("search"); 
}

function deleteBtn(){
	console.log("delete");
}

function presentTable(bogus_Json)
{
   bogus_Json = [{"userID": 2, "phone": "407555555", "email": "cole@gmail.com", "lastname": "Sil", "firstname": "Cole"}, {"userID": 2, "phone": "5553456789", "email": "jimmy@dublin.com", "lastname": "Joyce", "firstname": "James"}, {"userID": 1, "phone": "5553456789", "email": "ScottyBoy@gmail.com", "lastname": "Fitzgerald", "firstname": "Scott"}, {"userID": 1, "phone": "5553425678", "email": "peoplesElbow@gmail.com", "lastname": "Rock", "firstname": "The"}];
    
    
    var count = Object.keys(bogus_Json).length;
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
    
    for (i = 0; i < count; i++){ 
        txt += "<tr>";
        txt += "<td>" + bogus_Json[i].firstname + "</td>";
        txt += "<td>" + bogus_Json[i].lastname + "</td>";
        txt += "<td>" + bogus_Json[i].email + "</td>";
        txt += "<td>" + bogus_Json[i].phone + "</td>";
        /*for (i = 0; i < count; i++) {
            	txt += "<td>" + bogus_Json[i]+ "</td>";
                
        } */
        txt += "</tr>"
    }
    txt += "</table>"
    
    
    document.getElementById("view").innerHTML = txt;
    console.log("end of presentTable");
    
}