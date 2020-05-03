function menu() {
  let menu = document.querySelector(".navbar-nav");

  if (menu !== null) {
    let arrMenu = menu.children;

    for (let i = 0; i < arrMenu.length; i++) {
      if (window.location.href === arrMenu[i].children[0].href) {
        arrMenu[i].setAttribute("class", "active");
        arrMenu[i].style.backgroundColor = "lightgray";
      }
    }
  } //end if
}

menu();
