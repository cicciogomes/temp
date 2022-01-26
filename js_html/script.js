var box = document.querySelector(".container");
var pageX = document.getElementById("x");
var pageY = document.getElementById("y");

function updateDisplay(event) {
    pageX.innerText = event.pageX;
    pageY.innerText = event.pageY;
}

function mouseclick() {
    console.log('click')
}

function mouserelease() {
    console.log('no click')
}
box.addEventListener("mousedown", mouseclick);
box.addEventListener("mouseup", mouserelease);

box.addEventListener("mousemove", updateDisplay, false);
box.addEventListener("mouseenter", updateDisplay, false);
box.addEventListener("mouseleave", updateDisplay, false);