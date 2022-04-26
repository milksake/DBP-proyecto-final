function toggleMenu() {
    let menu = document.getElementById('toggle-menu');
    if (menu.style.display == "") {
        menu.style.display = "block";
    }
    else {
        menu.style.display = "";
    }
}