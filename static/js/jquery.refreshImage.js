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

            // deal with each of the matched images
            return this.each( function() 
            {
                ///////////////////
                // initializaion //
                ///////////////////

                // grab the current image
                var image = $(this);

                // first run, set image with default options
                if( image.data('refreshImage_options') == undefined ){

                    if(debug)
                        console.log("refreshImage: first-run. Using default " +
                            "options.");
                    
                    image.data('refreshImage_options', defaultOptions );
                }

                //////////////////////
                // handle arguments //
                //////////////////////

                // override default options if custom options are supplied
                if( typeof( arg ) == "object" ){

                    if(debug)
                        console.log("refreshImage: New options supplied. " +
                            "Overriding previous options.");

                    image.data('refreshImage_options',
                        $.extend( defaultOptions, arg ));

                // if the argument is a string, treat it as a command
                } else if( typeof( arg ) == "string" ){

                    if(debug)
                        console.log("refreshImage: argument is command.");

                    // if command is "start", start refreshing the image
                    if( arg == "start" ){
                    
                        if(debug)
                            console.log("refreshImage: 'start' command " +
                                "entered. Starting refresh cycle now.");

                        startRefreshing();

                    // if command is "stop", clear the timer to stop the
                    // refresh
                    } else if( arg == "stop" ){

                        if(debug)
                            console.log("refreshImage: 'stop' command entered."+
                                " Stopping refresh cycle.");

                        stopRefreshing();

                    // otherwise, the command is invalid
                    } else {
                        console.error( "refreshImage: invalid command: "+arg);
                        return -1;
                    }

                // if the argument is not an object or a string, error out
                } else {
                    console.error( "refreshImage: invalid arg type: " +
                        typeof(arg) );
                    return -1;
                }

                // if the argument was not a command, check the options to see
                // if the image needs to be updated now
                var options = image.data('refreshImage_options');
                if( options.start == true ){ 
                
                    if(debug)
                        console.log("refreshImage: option 'start' == true."
                            +" Starting refresh cycle.");

                    startRefreshing();
                }
               
                //////////////////
                // facilitators //
                //////////////////

                // startRefreshing()
                // begin refreshing the image immediately
                function startRefreshing()
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
                        setTimeout( function(){startRefreshing()}, options.interval);
                    image.data( 'refreshImage_timer', timer );
                }

                function stopRefreshing()
                {
                    if(debug)          
                        console.log("refreshImage: stopping. clearing timer.");

                    var timer = image.data('refreshImage_timer');
                    
                    if( timer != undefined ) clearTimeout( timer );
                }

            });
        }
    });
})(jQuery);
