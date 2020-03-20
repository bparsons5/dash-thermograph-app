$( window ).on( "load", function() {
    console.log("jquery working");

    // Operates the sliding sidebar
    $("#sidebar-btn").click(function(){
        $("#mainbar").toggleClass("mainbar-marginLeft");
    });

    // Toggle viewing the messages
    $("#notificationIconRow").click(function(){
        $("#notificationsDropdowns").toggleClass("notificationsVisible");
    });
    

    // Controls what gets displayed in the page-content
    $(".tabOption").click(function(el) {
        $(".contentSelected").removeClass("contentSelected");
        $("#" + $(el)[0].currentTarget.id + "-content")[0].classList.add("contentSelected")
    });
    
    // Controls the sidebar functionality during navigation
    $(".tabOption").click(function(el) {
        $(".tabSelected").removeClass("tabSelected");
        $(".submenuItemSelected").removeClass("submenuItemSelected");

        // is it a tab
        if (el.currentTarget.classList.contains('tab') === true) {
            // tab
            $(el)[0].currentTarget.classList.add("tabSelected");
        } else {
            // submenu item
            
            // first make parent of sub menu item the selected tab
            $("#" + $(el)[0].currentTarget.parentElement.previousElementSibling.id)[0].classList.add("tabSelected");
            
            // highlight the submenu item
            $(el)[0].currentTarget.classList.add('submenuItemSelected');
        }
    });

    $(".submenuTab").click(function(el) {
        $("#" + $(el)[0].currentTarget.id + " .submenuTabIcon").toggleClass("fa-angle-down fa-angle-up");
    });

});
