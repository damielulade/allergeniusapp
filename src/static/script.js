function detectOrientation() {
  var orientation = window.orientation;
  switch(orientation) {
    case 0:
    case 180:
      document.body.style.display='none';
      location.reload();
      setTimeout(function(){
        document.body.style.display=originalBodyStyle;
      }, 1);
      break;
    case -90:
    case 90:
      document.body.style.display='none';
      location.reload();
      setTimeout(function(){
        document.body.style.display=originalBodyStyle;
      }, 1);
      break;
  }
}

window.addEventListener("orientationchange", function () {
  detectOrientation();
});

// function detectResize() {
//   if(window.matchMedia("(orientation: portrait)").matches) {

//     var topbar = document.querySelector('.top-bar');
//     topbar.style.width = '100%';
    
//   }
// }

// window.addEventListener('resize', function() {
//     detectResize();
// });

document.addEventListener("DOMContentLoaded", function() {
  if (/Mobi/.test(navigator.userAgent)) {
    document.body.style.backgroundColor = 'rgb(255, 255, 255)';
    if(window.matchMedia("(orientation: portrait)").matches) {      
      var sidebar_right = document.querySelector('.sidebar-right');
      sidebar_right.style.display = 'none';

      var sidebar_left = document.querySelector('.sidebar-left');
      sidebar_left.style.display = 'none';

      var main = document.querySelector('.main');
      main.style.width = '100%';

      var accountname = document.querySelector('#accountname');
      accountname.style.color = 'rgb(0, 0, 0)';

      var topbar = document.querySelector('.top-bar');
      topbar.style.width = '100%';
      topbar.style.marginRight = '0%';
      topbar.style.marginLeft = '0%';

      var container = document.querySelector('.container');
      container.style.width = '100%';
      container.style.marginRight = '0%';
      container.style.marginLeft = '0%';

      var map_image = document.getElementById('mapimg');
      map_image.src = "static/staticmap2.png";

      var searchresults_image = document.getElementById('searchresults');
      searchresults_image.src = "static/searchresults2.png";  
    } else if (window.matchMedia("(orientation: landscape)").matches) {            

    }
  } else {
    var button_box = document.querySelector('.button-bar');
    button_box.style.display = 'none';

    var sidebar_right = document.querySelector('.sidebar-right');
    sidebar_right.style.backgroundColor = 'var(--appcolor)';

    var sidebar_left = document.querySelector('.sidebar-left');
    sidebar_left.style.backgroundColor = 'var(--appcolor)';
  }
}
);

function exampleQuery() {
  var query = document.getElementById("search-input").value;
  if (query == "american"){
    window.location.href = 'american';
  } else {
    window.location.href = 'search';
  }
}