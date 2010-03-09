/**
 * jQuery.refreshImage
 * Copyright (c) 2009 Oregon State Univerisity - info(at)osuosl.org | osuosl.org
 * licensed under GPLv3.
 * Date: 3/11/2009
 *
 * @projectDescription jquery extension for automatically refreshing an image.
 * @author Peter Krenesky -  kreneskyp(at)gmail.com
 * @version 1.0
 *
 * @id jQuery.refreshImage
 * @id jQuery.fn.refreshImage
 * @param {Object} settings Hash of settings, it is passed in to jQuery.refreshImage, none is required
 * @return {jQuery} Returns the same jQuery object, for chaining.
 *
 *
 * Notes:
 *  - The plugin loads each image using a different url because it is not possible to clear the image
 *    from the cache.  This will result in increase memory usage as time goes on.  If your browser
 *    does not properly dispose of the in memory cache it will grow indefinitely.  
 *
 *      Tested this in firefox.  Firefox3 has a cache size around 350megs.  It will garbage collect 
 *      the majority of the cache if it reaches that size.
 */

;(function($){
    $.refreshImage = {// defaults are public and can be overridden
        interval:60000, // how long inbetween refreshes, in milliseconds
        start:false     // start refresh immediately
    }

    jQuery.fn.refreshImage = function(settings){
        
        settings = $.extend( {}, $.refreshImage, settings );

        return this.each(function()
        {
            obj = $(this);
            counter = 0;
            timer = -1

            // Custom events bound to image
            if( !obj.ribound) {
                obj
                    .bind('start.refreshImage', start)          //starts or continues updates.
                    .bind('pause.refreshImage', pause)          //pauses updates indefinitely
                    .bind('refresh.refreshImage', refresh_now)  //refreshes image immediately
            }
            obj.ribound = true // prevents binding a second time


            // record the next time this image should refresh
            now = new Date().getTime();
            next_refresh = now + settings.interval;

            // start refreshing
            if( settings.start )
                timer = setTimeout(refresh_now, settings.interval);

            /* Start - starts periodic updates of the image.  If the 
                *         updates were previously running it continues
                *         from the old interval.  If the interval is passed
                *         then it refreshes immeditely and resets the timer */
            function start()
            {
                now = new Date().getTime();
                if (now > next_refresh) {
                    refresh_now();
                }
            }

            /* Pause - Stops updates. Timer expiration date is still saved
                *         so it can be continued later with start() */
            function pause() {
                clear();
            }

            /* Start - Immediately refreshes the page.  The interval is also reset */
            function refresh_now()
            {
                image_href = obj.attr('src');
            
                //safelog( "refreshImage: refreshing images" );
                //safelog( "refreshImage: Image url: " + obj.attr('src') );
                
                // images are being cached so we need to change the url by
                // adding a hashtag to it the following code accounts for a urls
                // that may or may not have a query string at the end

                // split the url at the query string
                matches = image_href.match(/^(.*)(\?.*)?$/);

                //reconstruct with hashtag before querystring
                href_counter = matches[1] + '#' + counter + matches[2]
                obj.attr('src', href_counter);
                counter = counter + 1;

                // record the next time this image should refresh
                now = new Date().getTime();
                next_refresh = now + settings.interval;


                // set timer for refresh
                clear();
                timer = setTimeout(refresh_now, settings.interval);
            }

            function clear()
            {
                if( timer != -1 ) clearTimeout(timer);
            };

        });
    };
})( jQuery );
