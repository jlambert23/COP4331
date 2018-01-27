var url = "http://18.219.16.244";
var ext = ".py"


function test() {
    var userName = document.getElementById("userNameText").value;
    var password = document.getElementById("passwordText").value;

    if (userName === "") {
        alert("Please insert username");
        return;
    }
    else if (password === "") {
        alert("Please insert password");
        return;
    }

    hideOrShow("successBox", true);

    var jsonPayload = '{"username" : "' + userName + '", "password" : "' + hashPassword(password) + '"}';

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url + "/comm" + ext);
    xhr.setRequestHeader("Content-type", "application/json; charset=UTF-8");

    // Event handler to asynchronously retrieve response.
	xhr.onreadystatechange = function() {
		if (xhr.readyState == 4 && xhr.status == 200) {
            console.log(xhr.responseText);
            
            try {
                var jsonObject = JSON.parse(xhr.responseText);
            }
            catch (err) {
                console.log(err);
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

