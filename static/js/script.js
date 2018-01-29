
$(function() {
    $('button').click(function() {
        var currs = $('#txtCurrenices').val();
        $.ajax({
            url: '/currs',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
