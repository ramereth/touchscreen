(function($){
    
    $.fn.extend({

        refreshImage: function( arg, debug )
        {            
            // flag debug mode if it's value is "debug"
            debug = debug == "debug";
            
            if(debug) console.info("refreshImage: debug mode on");

            // default options
            var defaultOptions = {
                interval: 30000,    // default refresh interval
                start: false        // start the refresh right away?
            }

            // for each of the matched elements, do the specified refresh task
            return this.each(function() 
            {
                // capture the current image
                var image = $(this);

                // set image with default options first-run
                if( image.data('refreshImage_options') == undefined ){

                    if(debug)
                        console.log("refreshImage: first-run. Using default " +
                            "options.");
                    
                    image.data('refreshImage_options', defaultOptions );
                }

                // override default options if custom options are supplied
                if( typeof( arg ) == "object" ){

                    if(debug)
                        console.log("refreshImage: custom options supplied. " +
                            "Overriding previous options.");

                    image.data('refreshImage_options',
                        $.extend( defaultOptions, arg ));

                // if the argument is a string, treat it as a command
                } else if( typeof( arg ) == "string" ){

                    if(debug)
                        console.log("refreshImage: handling command '%s'", arg);

                    // if command is "start"
                    if( arg == "start" ) refreshNow();

                    // clear the timeout if the command is "stop"
                    else if( arg == "stop" ){

                        if(debug)
                            console.log("refreshImage: stopping. clearing "+
                                "timers.");
                            
                        clearTimeout( image.data('refreshImage_timer') );
                        
                    // if command is "now"
                    } else if( arg == "now" );
                    
                    // otherwise, the command is invalid
                    else {
                        
                        if( debug )
                            console.error( "refreshImage: invalid command: " +
                                arg );
                            
                        return -1;
                    }

                // if the argument is not an object or a string, error out
                } else {
                    
                    if(debug)
                        console.error( "refreshImage: invalid arg type: "+arg );
                        
                    return -1;
                }

                var options = image.data('refreshImage_options');

                if( options.start == true ) refreshNow();
                
                function refreshNow()
                {
                    var options = image.data('refreshImage_options');
                    
                    // refresh the image if a src is defined
                    if( image.attr('src') != undefined ){
                        
                        // get rid of any previous refresh image cruft
                        var cleanSrc = image.attr('src').replace(/\#.*$/,"");

                        // generate a random hash
                        var newSrc = cleanSrc + '#' + Math.random();

                        // set the new source
                        image.attr( 'src', newSrc );

                        if(debug)
                            console.log("refreshImage: Refreshed image to " +
                            newSrc );
                            
                    } else
                        if(debug) console.warn("refreshImage: src undefined.");

                    // set the timout, and save it in the element
                    var timer =
                        setTimeout( function(){refreshNow()}, options.interval);
                    image.data( 'refreshImage_timer', timer );
                }
            });
        }
    });
})(jQuery);
