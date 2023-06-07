function detectOrientation() {
  var originalBodyStyle = getComputedStyle (document.body).getPropertyValue('display');

  var orientation = window.orientation;
  switch(orientation) {
    case 0:
    case 180:
      document.body.style.display='none';
      location.reload();
      setTimeout(function(){
        document.body.style.display = originalBodyStyle;
      }, 1);
      break;
    case -90:
    case 90:
      document.body.style.display='none';
      location.reload();
      setTimeout(function(){
        document.body.style.display = originalBodyStyle;
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
      const sidebar_right = document.querySelector('.sidebar-right');
      sidebar_right.style.display = 'none';

      const sidebar_left = document.querySelector('.sidebar-left');
      sidebar_left.style.display = 'none';

      const main = document.querySelector('.main');
      main.style.width = '100%';

      const account_name = document.querySelector('#account-name');
      account_name.style.color = 'rgb(0, 0, 0)';

      const top_bar = document.querySelector('.top-bar');
      top_bar.style.width = '100%';
      top_bar.style.marginRight = '0%';
      top_bar.style.marginLeft = '0%';

      const container = document.querySelector('.container');
      container.style.width = '100%';
      container.style.marginRight = '0%';
      container.style.marginLeft = '0%';

      const map_image = document.getElementById('map-img');
      map_image.src = "/static/static_map2.png";

      const search_results_image = document.getElementById('search-results');
      search_results_image.src = "/static/search_results2.png";

    } else if (window.matchMedia("(orientation: landscape)").matches) {

    }
  } else {

    var sidebar_right = document.querySelector('.sidebar-right');
    sidebar_right.style.display = 'inline';
    sidebar_right.style.backgroundColor = 'var(--appcolor)';

    var sidebar_left = document.querySelector('.sidebar-left');
    sidebar_left.style.display = 'inline';
    sidebar_left.style.backgroundColor = 'var(--appcolor)';

    var sidebar_left = document.querySelector('.main');
    sidebar_left.style.width = '40%';
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

window.onload = function() {};