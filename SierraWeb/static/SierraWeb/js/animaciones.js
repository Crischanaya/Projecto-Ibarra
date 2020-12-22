$(document).ready(function(){
    
    $(".contenido-contacto").mouseenter(function(){
        $(this).animate({height: "250px"});
        $(".contenido-contacto a").animate({padding: "30px 0px 30px 0"});
    });

    $(".contenido-contacto").mouseleave(function(){
        $(this).animate({height: "185px"});
        $(".contenido-contacto a").animate({padding: "10px 0px 10px 0"});
    });

    $('.zoom-img').hover(function() {
        $(this).animate({height: "220px"});
        $(this).addClass('transition');
    
    }, function() {
        $(this).removeClass('transition');
        $(this).animate({height: "200px"});
    });

    $(".menu-movil").click(function(){
        $('#header').toggle('slow');
    });

});