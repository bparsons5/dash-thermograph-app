$( window ).on( "load", function() {
    console.log("jquery working");
    $("#sidebar-btn").click(function(){
        $("#mainbar").toggleClass("mainbar-marginLeft");
    });
});
