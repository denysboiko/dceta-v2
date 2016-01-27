(function($){

    $('.send').click(function (e) {
        e.preventDefault();
        $(this).addClass('btn-disabled');
        $(this).prop('disabled', true);
        $.post("send-order.php", $(this).parents(".send-form").serialize(),function (response) {

        });
    });

    // Menu settings
    $('#menuToggle, .menu-close').on('click', function(){
        $('#menuToggle').toggleClass('active');
        $('body').toggleClass('body-push-toleft');
        $('#theMenu').toggleClass('menu-open');
    });

    // CAROUSEL PREVIEW

    (function(){
        var next = $("#dceta-slider .item").eq(1).find("h2").text();
        var prev = $("#dceta-slider .item ").eq($(this).length + 1).find("h2").text();

        $('#dceta-slider').on('slid.bs.carousel', function () {
            next = $("#dceta-slider .item.active").next(".item").find("h2").html();
            if (typeof next == "undefined") next=$("#dceta-slider .item").eq(0).find("h2").text();

            prev = $("#dceta-slider .item.active").prev(".item").find("h2").html();
            if (typeof prev == "undefined") prev=$("#dceta-slider .item").eq($(this).length+1).find("h2").text();
            $(".carousel-control.left div h3").html(prev);
            $(".carousel-control.right div h3").html(next);
        });

        $(".carousel-control.left div h3").html(prev);
        $(".carousel-control.right div h3").html(next);

    })();





})(jQuery);
