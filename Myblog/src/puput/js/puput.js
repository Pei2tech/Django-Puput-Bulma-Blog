class Handler {
    constructor() {
    }

    /**
     *  init()  : bind listen event
     * @memberof Handler
     */
    init() {
         document.querySelectorAll('.parent .sub').forEach(element=>{
             element.style.display='none';
        });
         document.querySelectorAll(".parent a .open-sub").forEach(element=>{
             element.addEventListener("click", event => {
                 this._handleArchive(event);
             });
        });
    }

    _handleArchive(event){
        event.preventDefault();
        if (event.target.closest('.parent').classList.contains('active')) {
            event.target.closest('.parent').querySelector('.sub').style.display='none';
            event.target.closest('.parent').classList.remove('active');
        } else {
            event.target.closest('.parent').classList.add('active');
            event.target.closest('.parent').querySelector('.sub').style.display='block';
        }
    }
}


document.addEventListener("DOMContentLoaded", ()=> {
    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {

      // Add a click event on each of them
      $navbarBurgers.forEach( el => {
        el.addEventListener('click', () => {

          // Get the target from the "data-target" attribute
          const target = el.dataset.target;
          const $target = document.getElementById(target);

          // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
          el.classList.toggle('is-active');
          $target.classList.toggle('is-active');
        });
      });
    }
});

(function() {
  let handler=new Handler();
  handler.init();
}());