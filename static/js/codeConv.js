submit = document.getElementById('submit')
codeInput = document.getElementById('codeInput')

submit.onclick = function()  {
    if(((codeInput.value).length) > 0) {
        docGen((codeInput.value))
    }
    else {
        alert("You can't submit without entering Code")
    }
}

function docGen(code) {
    let xhr = new XMLHttpRequest();

    console.log('inside codeConv')
    xhr.open("POST", "/CODECONV", true);
    //Send the proper header information along with the request
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onload = function () {
            console.log('inside codeConv Load')
            if (this.status == 200) {
                    // console.log(this.responseText)
                    outputCode = this.responseText
                    outputCode = JSON.parse(outputCode)
                    console.log(outputCode)

                    document.getElementById('codeOutput').value = outputCode
            }
            else {
                    console.log("inside codeConv else")
            }
    }
    params = { "codeInput": code }
    xhr.send(JSON.stringify(params));
}

let menu = document.getElementById('menu_icon');
let navbar = document.getElementById('navbar-nav');

menu.onclick = () => {
    navbar.classList.toggle('open');
}

let copy = document.getElementById('copybtn');
let codeOutput = document.getElementById('codeOutput');
let copied = document.getElementById('copied');

copy.onclick = () => {
    codeOutput.select();
    document.execCommand('copy');
    copied.style.display="block";
    window.getSelection().removeAllRanges();
    setTimeout(function() {
        copied.style.display="none";
    }, 2500);
}

