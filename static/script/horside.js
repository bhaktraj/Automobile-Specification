const buttonRight = document.getElementById('slideRight');
    const buttonLeft = document.getElementById('slideLeft');

    buttonRight.onclick = function () {
      document.getElementById('wrapper').scrollLeft += 90;
    };
    
    buttonLeft.onclick = function () {
      document.getElementById('wrapper').scrollLeft -= 90;
    };