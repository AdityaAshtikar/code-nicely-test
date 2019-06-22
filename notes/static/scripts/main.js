$('#post-form').on('submit', function (event) {
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_note();
});

function create_note() {
    console.log("create post is working!") // sanity check

    // ajax

    $.ajax({
        url: "",
        type: "POST",
        data: { title: $('#note-title').val(), text: $('#note-text').val() },
        success: function (json) {
            $('#note-title').val('')
            $('#note-text').val('')
            $("#notes-data").prepend("<div class='card' style='width: 18rem;'><div card-body><h5 class='card-title'>" + json.title + "</h5><p class='card-text'>" + json.text + "</p><p class='card-text'>" + json.created + "</p></div></div>");
        },
        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });

    console.log($('#note-title').val())
    console.log($('#note-text').val())
};