$(function() {
   var addMine = function(text) {
        var before = '<div class="row chat"><div class="col-md-offset-7 col-md-5 message mine"><span>'
        var after = '</span></div></div>'
        var total = before + text + after
        var elem = $(total)
        $('#chat-window-content').append(elem)
    }

    var addTheirs = function(text) {
        var before = '<div class="row chat"><div class="col-md-5 message theirs"><span>'
        var after = '</span></div></div>'
        var total = before + text + after
        var elem = $(total)
        $('#chat-window-content').append(elem)
    }

    $('#chat-input').keypress(function(e) {
        if (e.which == '13') {
            var text = $(this).val()
            addMine(text)

            $(this).val("")
            $.post('listen', {text: text}, function(data) {
                console.log(data)
                addTheirs(data.response)
            })
        }

    })
})