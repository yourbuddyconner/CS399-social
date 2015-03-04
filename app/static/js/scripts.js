
$(document).ready(function() {/* off-canvas sidebar toggle */
    $('[data-toggle=offcanvas]').click(function() {
        //if visible, then not visible, else visible
      	$(this).toggleClass('text-center text-right');
        //switch the icon from left to right or reverse
        $(this).find('i').toggleClass('fa-chevron-right fa-chevron-left');
        //toggle off-canvas 
        $('.row-offcanvas').toggleClass('active');
        //Shrink the sidebar
        $('#sidebar').toggleClass('col-sm-1 col-sm-2');
        $('#main').toggleClass('col-sm-10 col-sm-11');
        //make large visible
        $('#lg-menu').toggleClass('hidden-xs').toggleClass('visible-xs');
        //while making small hidden
        $('#xs-menu').toggleClass('visible-xs').toggleClass('hidden-xs');
        $('#btnShow').toggle();
    });
});