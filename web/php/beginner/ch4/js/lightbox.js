//complete code listing for js/lightbox.js
//edit existing function
function init() {
    var lightboxElements = "<div id='lightbox'>";
    lightboxElements += "<div id='overlay' class='hidden'></div>";
    lightboxElements += "<img class='hidden' id='big-image' />";
    lightboxElements += "</div>";
    document.querySelector("body").innerHTML += lightboxElements;
	//new code: register toggle as event handler
	var bigImage = document.querySelector("#big-image")
	bigImage.addEventListener("click",toggle, false);

    //add a new function call here
    prepareThumbs();
}

//edit existing function
function toggle(event) {
    //which image was clicked
    var clickedImage = event.target;
    var bigImage = document.querySelector("#big-image");
    var overlay = document.querySelector("#overlay");
    bigImage.src = clickedImage.src;
    //if overlay is hidden, we can assume the big image is hidden
    if (overlay.getAttribute("class") === "hidden") {
        overlay.setAttribute("class", "showing");
        bigImage.setAttribute("class", "showing");
    } else {
        overlay.setAttribute("class", "hidden");
        bigImage.setAttribute("class", "hidden");
    }
}

//declare new function
function prepareThumbs() {
    var imgDivElements = document.querySelectorAll("div#thumb");

    while (i < imgDivElements.length) {
        var div = imgDivElements[i];

        var image = div.querySelector("img");
        image.addEventListener("click", toggle, false);
        i += 1;
    }
}

document.addEventListener("DOMContentLoaded", init, false);