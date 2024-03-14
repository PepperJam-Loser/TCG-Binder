function toggleDropdown(menuId, iconId, defaultIcon) {
    var menu = document.getElementById(menuId);
    var icon = document.getElementById(iconId);
    if (menu.style.display === "block") {
        menu.style.display = "none";
        icon.innerHTML = '<i class="fas ' + defaultIcon + '"></i>'; // Change icon back to default
    } else {
        menu.style.display = "block";
        icon.innerHTML = '<i class="fas fa-times"></i>'; // Change icon to X
    }
    // Drop down menu doesn't collapse unless x is clicked or user clicks anywhere on the screen
    event.stopPropagation();
}

// Make it so when a user clicks one menu then clicks another both menus don't collapse until click anywhere on screen
document.body.addEventListener('click', function(event) {
    var menu1 = document.getElementById('menu1');
    var menu2 = document.getElementById('menu2');
    var menu1Icon = document.getElementById('menu1Icon');
    var menu2Icon = document.getElementById('menu2Icon');
    var clickedElement = event.target;
    var isMenu1Icon = clickedElement.id === 'menu1Icon';
    var isMenu2Icon = clickedElement.id === 'menu2Icon';
    if (!isMenu1Icon && !menu1.contains(clickedElement)) {
        menu1.style.display = 'none';
        menu1Icon.innerHTML = '<i class="fas fa-bars"></i>';
    }
    if (!isMenu2Icon && !menu2.contains(clickedElement)) {
        menu2.style.display = 'none';
        menu2Icon.innerHTML = '<i class="fas fa-user-circle"></i>';
    }
});