var url = window.location.href; //"http://18.219.16.244";
var ext = ".py"

function login() {
    var userName = document.getElementById("userNameText").value;
    var password = document.getElementById("passwordText").value;

    if (userName === "" || password === "") {
        hideOrShow("warningBox", true);
        return;
    }
    
    // Send json to backend API.
    var jsonPayload = '{"username" : "' + userName + '", "password" : "' + hashPassword(password) + '"}';   
    // var jsonReceive = sendJSON(jsonPayload, url + "API/login" + ext);


    /*---------------------------------------------------------------------------*/
    /*                          The worst code ever...                           */
    /*---------------------------------------------------------------------------*/
    
    // Configure AJAX
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url + "API/login" + ext);
    xhr.setRequestHeader("Content-type", "application/json; charset=UTF-8");

    // Event handler to asynchronously retrieve response.
	xhr.onreadystatechange = function() {
		if (xhr.readyState == 4 && xhr.status == 200) {
            console.log(xhr.responseText);

            try {
                var jsonReceive = JSON.parse(xhr.responseText);
            }
            catch (err) {
                console.log(err);
                hideOrShow("warningBox", true);
            }
            
            if (!jsonReceive.hasOwnProperty('id')) {
                hideOrShow("warningBox", true);
                return;
            }
                
            
            hideOrShow("loginForm", false);
            
		}
	}

    xhr.send(jsonPayload);
}    
    /*

    console.log(jsonReceive);
    
    // if (jsonReceive.hasOwnProperty('id')) {
		// hideOrShow("warningBox", true);
        // return;
	// }

	currentuserid = jsonReceive.id;
    jsonPayload ='{"currentuserid" : "2"}'
    jsonReceive = sendJSON(jsonPayload, url + "API/QueryContacts" + ext);

    presentTable();
    hideOrShow("loginForm", false);
    */


function sendJSON(jsonPayload, pyScript) {
    // Configure AJAX
    var xhr = new XMLHttpRequest();
    xhr.open("POST", pyScript, false);
    xhr.setRequestHeader("Content-type", "application/json; charset=UTF-8");

    // Event handler to asynchronously retrieve response.
	xhr.onreadystatechange = function() {
		if (xhr.readyState == 4 && xhr.status == 200) {
            console.log(JSON.parse(xhr.responseText));

            try {
                return JSON.parse(xhr.responseText);
            }
            catch (err) {
                console.log(err + "ERROR XML/JSON");
                return null;
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
	var firstName = document.getElementById("firstNameBox").value;
    var lastName = document.getElementById("lastNameBox").value;
    var email = document.getElementById("emailBox").value;
    var phoneNum = document.getElementById("phoneBox").value;
    
    console.log(firstName); console.log(lastName); console.log(email); console.log(phoneNum);
    
    var jsonPayload = '{"firstName" : "' + firstName + '", "LastName" : "' + lastName + '", "email" : "' + email + '", "phone" : "' + phoneNum + '"}';
    var jsonRecieve = "";
    
    bogus_Json = [{"currentuserid": 2, "phone": "111111", "email": "asdf@gmail.com", "lastname": "Sil", "firstname": "Cole"}, {"currentuserid": 2, "phone": "222222", "email": "zxcv@dublin.com", "lastname": "Joyce", "firstname": "James"}, {"currentuserid": 1, "phone": "333333333", "email": "qwer@gmail.com", "lastname": "Fitzgerald", "firstname": "Scott"}, {"currentuserid": 1, "phone": "44444444", "email": "fghj@gmail.com", "lastname": "Rock", "firstname": "The"}];
    
    presentTable(bogus_Json);
    
    
}

function searchBtn(){
	console.log("search"); 
}


    //count = 0; console.log("FIRE AWAY");
   /* $('.btn-danger').click(function() {
        var row = $(this).closest("tr");
        var td = row.find("td");
        $.each(td, function() {
        console.log($(this).text());
    });
    }) */
    
    
	/*$('#rowBtn').click(function(){
        var row = $(this).closest("tr");
        var td = row.find("td");
        $.each(td, function() {
        console.log($(this).text());
    });
    $(this).parents('tr').remove();
}) */



function presentTable()
{
    hideOrShow("queryForm", true);
    bogus_Json = [{"userid": 2, "phone": "407555555", "email": "cole@gmail.com", "lastname": "Sil", "firstname": "Cole"}, {"currentuserid": 2, "phone": "5553456789", "email": "jimmy@dublin.com", "lastname": "Joyce", "firstname": "James"}, {"currentuserid": 1, "phone": "5553456789", "email": "ScottyBoy@gmail.com", "lastname": "Fitzgerald", "firstname": "Scott"}, {"currentuserid": 1, "phone": "5553425678", "email": "peoplesElbow@gmail.com", "lastname": "Rock", "firstname": "The"}];
    
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
        txt += "<td>" + "<button id='rowBtn' style='margin-left:2%;' type='button' class='btn btn-danger'>Delete</button>" + "</td>";
        /*for (i = 0; i < count; i++) {
            	txt += "<td>" + bogus_Json[i]+ "</td>";
                
        } */
        txt += "</tr>"
    }
    txt += "</table>"
    
    
    document.getElementById("view").innerHTML = txt;
    console.log("end of presentTable");
    
}