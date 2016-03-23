//Complete code for js/editor.js
//declare new function
function checkTitle (event) {
    var title = document.querySelector("input[name='title']");
    var warning = document.querySelector("form #title-warning");
    //if title is empty...
    if (title.value === "") {
        //preventDefault, ie don't submit the form
        event.preventDefault();
        //display a warning
        warning.innerHTML = "*You must write a title for the entry";
    }
}


function updateEditorMessage () {
   var p = document.querySelector("#editor-message");
    p.innerHTML = "Changes not saved!";

}


function init(){
    console.log("!");
    var editorForm = document.querySelector("form#editor");
    var title = document.querySelector("input[name='title']");
    //this will prevent standard browser treatment of the required attribute
    title.required = false;
    title.addEventListener("keyup", updateEditorMessage, false);
    editorForm.addEventListener("submit", checkTitle, false);
}


document.addEventListener("DOMContentLoaded", init, false);
