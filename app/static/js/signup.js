function checkUsername() {
    var username = document.getElementById("usernameInput").value;
    if (username.length === 0) {
        document.getElementById("usernameStatus").innerHTML = "";
        return;
    }

    fetch(`/check-username/?username=${username}`)
    .then(response => response.json())
    .then(data => {
        let statusElement = document.getElementById("usernameStatus");
        if (data.available) {
            statusElement.innerHTML = "<span style='color:green;'>✔ Username is available!</span>";
        } else {
            statusElement.innerHTML = "<span style='color:red;'>✖ Username is already taken!</span>";
        }
    });
}