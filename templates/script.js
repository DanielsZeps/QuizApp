function backgroundChange(value) {
    document.body.style.backgroundColor = value;
}

function randomColor() {
    return Math.floor( Math.random() * 256);
}

function renderBackground() {
    var temp = "rgb(" + randomColor() + ", " + randomColor() + ", " + randomColor() + ")";
    backgroundChange(temp);
}

function loadDoc() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        document.body.innerHTML = this.responseText;
    }
    xhttp.open("GET", "textResponse");
    xhttp.send();
}

function bodyload() {
    renderBackground();
    setInterval(renderBackground, 1000);
}