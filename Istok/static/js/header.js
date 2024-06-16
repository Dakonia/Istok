
$(document).ready(function() {
    var modal = $('#loginModal');
    var loginFormContainer = $('#loginFormContainer');
    var registerFormContainer = $('#registerFormContainer');
    var registerPrompt = $('#registerPrompt');

    $('#openLoginModalBtn').click(function() {
        loginFormContainer.show();
        registerFormContainer.hide();
        registerPrompt.show();
        modal.removeClass('register-open'); 
        modal.show();
    });

    $('.close').click(function() {
        modal.hide();
    });
    $('.close-login').click(function() {
        modal.hide();
    });

    $('#showRegisterForm').click(function() {
        loginFormContainer.hide();
        registerFormContainer.show();
        registerPrompt.hide();
        modal.addClass('register-open'); 
    });

    $('#showRegisterFormFromLogin').click(function() {
        loginFormContainer.hide();
        registerFormContainer.show();
        modal.addClass('register-open'); 
    });

    $(window).click(function(event) {
        if ($(event.target).is(modal)) {
            modal.hide();
        }
    });
});
