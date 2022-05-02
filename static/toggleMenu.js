function toggleMenu() {
    let menu = document.getElementById('toggle-menu');
    if (menu.style.flexGrow == "1") {
        menu.style.flexGrow = "0";
        menu.style.color = "var(--color2)";
    }
    else {
        menu.style.flexGrow = "1";
        menu.style.color = "white"
    }
}