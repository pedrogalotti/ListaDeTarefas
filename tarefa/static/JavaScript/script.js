$(document).ready(function() {

    var baseUrl = 'http://127.0.0.1:8000/';
    var filter = $('#filter');

    $(filter).change(function(){
        var filter = $(this).val();

        window.location.href = baseUrl + 'home/?filter=' + filter;
    });

});