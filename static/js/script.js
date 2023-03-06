let menu = document.getElementById('menu_icon');
let navbar = document.getElementById('navbar-nav');

menu.onclick = () => {
    navbar.classList.toggle('open');
}