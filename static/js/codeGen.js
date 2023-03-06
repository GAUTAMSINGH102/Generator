submit = document.getElementById('submit')
textInput = document.getElementById('textInput')

submit.onclick = function()  {
    if(((textInput.value).length) > 0) {
        codeGen((textInput.value))
    }
    else {
        alert("You can't submit without Entering Text")
    }
}

function codeGen(text) {
    let xhr = new XMLHttpRequest();

    console.log('inside codeGen')
    xhr.open("POST", "/CODEGEN", true);
    //Send the proper header information along with the request
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onload = function () {
            console.log('inside CodeGen Load')
            if (this.status == 200) {
                    // console.log(this.responseText)
                    outputCode = this.responseText
                    outputCode = JSON.parse(outputCode)
                    console.log(outputCode)

                    document.getElementById('outputCode').value = outputCode
            }
            else {
                    console.log("inside codeGen else")
            }
    }
    params = { "textInput": text }
    xhr.send(JSON.stringify(params));
}


let menu = document.getElementById('menu_icon');
let navbar = document.getElementById('navbar-nav');

menu.onclick = () => {
    // alert('hi')
    navbar.classList.toggle('open');
}


let copy = document.getElementById('copybtn');
let outputCode = document.getElementById('outputCode');
let copied = document.getElementById('copied');

copy.onclick = () => {
    outputCode.select();
    document.execCommand('copy');
    copied.style.display="block";
    window.getSelection().removeAllRanges();
    setTimeout(function() {
        copied.style.display="none";
    }, 2500);
}
