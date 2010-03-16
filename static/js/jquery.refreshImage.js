/**
 * jQuery.refreshImage
 * Copyright (c) 2010 Oregon State Univerisity - info(at)osuosl.org | osuosl.org
 * licensed under GPLv3.
 * Date: march 12th 2010
 *
 * @projectDescription jQuery extension for automatically refreshing an image.
 * @author Rob McGuire-Dale (rob(at)osuosl.org)
 * @version 1.0
 *
 * @id jQuery.refreshImage
 * @id jQuery.fn.refreshImage
 *
 * USAGE:
 * 
 *  $('.images').refreshImage({interval:<milliseconds>,start:true|false}|"start"|"now"|"stop", ["debug"]);
 * 
 *  {interval:<milliseconds>, start:true|false}:
 *      This is a dictionary of settings specifying the refresh interval and
 *      whether or not to start the refresh cycle right away. These settings are
 *      optional. If none are set, defaults will be used. (30 second interval
 *      and does not start the cycle)
 *
 *  "start"
 *      Starts the refresh cycle, but does NOT refresh immediately.
 *
 *  "now"
 *      Starts the refresh cycle and refreshes immediately.
 *
 *  "stop"
 *      Stops the refresh cycle.
 *
 * 
 * EXAMPLES:
 *
 *  $('.images').refreshImage({interval:30000, start:true});
 *      Sets the refresh interval to 30 seconds, and sarts the refresh cycle,
 *      but does not refresh immediately. 
 *
 *  $('.images').refreshImage("start");
 *      Starts the refresh cycle, but will not immediately refresh.
 *
 *  $('.images').refreshImage("now");
 *      Starts the refresh cycle, AND refreshes immediately.
 *
 *  $('.images').refreshImage("stop");
 *      Stops the refresh cycle.
 *
 * 
 * RETURNS:
 * 
 *  This returns the same matched jQuery objects, for chaining. If there is any
 *  kind of error, it will return a -1.
 *
 *
 * NOTES:
 * 
 *  The plugin loads each image using a different url because it is not possible
 *  to clear the image from the browser's cache. This will result in increased
 *  memory usage as time goes on.  If your browser does not properly dispose of
 *  the cache it will grow indefinitely.  
 *
 *  Tested this in firefox.  Firefox3 has a cache size around 350megs. It will
 *  garbage collect the majority of the cache if it reaches that size.
 *
 *  This plugin is a drop-in (almost) rewrite of the refreshImage plugin written
 *  by Peter Krenesky (kreneskyp(at)gmail.com) in March 2010.
 */

(function($){
    
    $.fn.extend({

        refreshImage: function( arg, debug )
        {            
            // flag debug mode if the debug argument's value is "debug"
            //debug = debug == "debug";
            debug = false;
            
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
                                "entered. Starting refresh cycle.");

                        startTimer();

                    // if command is "now", start refreshing the image
                    } else if( arg == "now" ){
                    
                        if(debug)
                            console.log("refreshImage: 'now' command " +
                                "entered. Refreshing NOW.");

                        refreshNow();

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
                        console.log("refreshImage: option 'start' == true." +
                            " Starting refresh cycle."
                        );

                    startTimer();
                }
               
                //////////////////
                // facilitators //
                //////////////////

                // refreshNow()
                // begin refreshing the image immediately
                function refreshNow()
                {                    
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

                    // set the timout
                    startTimer();
                }

                // stop the refresh cycle by clearing the timer
                function stopRefreshing()
                {
                    if(debug)          
                        console.log("refreshImage: clearing timer.");

                    var timer = image.data('refreshImage_timer');
                    
                    if( timer != undefined ) clearTimeout( timer );
                }

                // set the timeout to start the refresh cycle
                function startTimer()
                {
                    var options = image.data('refreshImage_options');
                    stopRefreshing(); // clear the old timer
                    var timer = setTimeout(
                        function(){refreshNow()},
                        options.interval
                    );
                    image.data( 'refreshImage_timer', timer );
                    if(debug)          
                        console.log("refreshImage: timer started. Next refresh"+
                            " in "+options.interval+" milliseconds."
                        );
                }
            });
        }
    });
})(jQuery);
