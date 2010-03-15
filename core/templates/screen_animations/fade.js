function fade_in(screen) {
    id = screen['id']
    var $screen = $('#'+id);

    //first move the screen into place
    $screen.css('left',0);
    $screen.css('top',0);

    //animate fading in of background
    $screen.children('.background').fadeIn(500, function(){
        $screen.children('.content').fadeIn(750);
    });
    
    return 1250
}

function fade_out(screen) {
    id = screen['id']
    var $screen = $('#'+id);

    //fade the contents out
    $screen.children('.content').fadeOut(750, function(){
        //fade the background out
        $screen.children('.background').fadeOut(750, function(){
            //move the box off the screen
            $screen.css('left',-100-Screen.getViewportWidth());
        });
    });

    return 1500;
}