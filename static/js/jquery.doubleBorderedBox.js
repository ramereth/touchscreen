/**
 * jQuery.doubleBorderedBox
 * Copyright (c) 2009 Oregon State Univerisity - info(at)osuosl.org | osuosl.org
 * licensed under GPLv3.
 * Date: 3/11/2009
 *
 * @projectDescription jquery extension for adding two borders, with different colors to an object.  This is used for creating borders that make boxes stand out more from the certain types of patterned background
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
 *   The div will be repositioned as absolutely within the new div.  The new Div will also be absolutely positioned.
 */

;(function($){
    $.doubleBorderedBox = {// defaults are public and can be overridden
        outer_border: '#ffffff',
        inner_border: '#000000'
    }

    jQuery.fn.doubleBorderedBox = function(settings) {
        settings = $.extend( {}, $.doubleBorderedBox, settings );

        return this.each(function(){
            $pane = $(this);

            //save all css needed to place the wrapper
            height_ = $pane.outerHeight();
            width_ = $pane.outerWidth();
            top_ = $pane.css('top');
            left_ = $pane.css('left');
            right_ = $pane.css('right');
            bottom_ = $pane.css('bottom');
            console.log(top_, left_, right_, bottom_);

            //modify positioning css
            $pane.css({
                position:'absolute',
                top:1,
                left:1
            });

            //get original background settings
            backgroundcolor = $pane.css('background-color');

            div = $('<div></div>');
            div.css ({
                position:'absolute',
                border:'1px solid' + settings.outer_border,
                'background-color':settings.inner_border,
                height:height_,
                width:width_,
                padding:'1px',
                top:top_,
                left:left_,
                right:right_,
                bottom:bottom_
            });
            $pane.replaceWith(div);
            console.log($pane.css());
            div.append($pane);
            console.log(div.html());
        });
    };
})( jQuery );