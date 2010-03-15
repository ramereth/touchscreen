function {{animation.hash}}_in(screen) {
    id = screen['id']
    duration = 1000;
    $('#'+id).animate({left:0}, duration );
    return duration;
}

function {{animation.hash}}_out(screen) {
    id = screen['id']
    duration = 1000;
    $('#'+id).animate({left:-100-screenWidth()}, duration );
    return duration;
}