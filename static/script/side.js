var button = document.getElementById('slideRight');
button.onclick = function () {
    var container = document.getElementsByClassName('wrapper');
    sideScroll(container,'right',25,100,10);
};

var back = document.getElementById('slideLeft');
back.onclick = function () {
    var container = document.getElementsByClassName('wrapper');
    sideScroll(container,'left',25,100,10);
};

function sideScroll(element,direction,speed,distance,step){
    scrollAmount = 0;
    var slideTimer = setInterval(function(){
        if(direction == 'left'){
            element.scrollLeft -= step;
        } else {
            element.scrollLeft += step;
        }
        scrollAmount += step;
        if(scrollAmount >= distance){
            window.clearInterval(slideTimer);
        }
    }, speed);
}