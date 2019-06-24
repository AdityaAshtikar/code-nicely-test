$('#post-form').on('submit', function (event) {
    event.preventDefault();
    create_note();
});

function create_note() {
    // ajax

    $.ajax({
        url: "",
        type: "POST",
        data: { title: $('#note-title').val(), text: $('#note-text').val() },
        success: function (json) {
            console.log(json)
            $('#note-title').val('')
            $('#note-text').val('')
            $("#notes-data").prepend("<div class='card col-sm-6' style='width: 16rem;'><div card-body><h5 class='card-title'>" + json['title'] + "</h5><p class='card-text'>" + json['text'] + "</p><p class='card-text'>" + json['created'] + "</p></div></div>");
        },
        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

function share(e) {
    e.preventDefault()
    name = document.getElementById('personName').value;
    $.ajax({
        url: "showPeople",
        type: "POST",
        data: { name: name },
        success: function (json) {
            $('#personName').append("<select></select>");
            for (var k in json) {
                console.log(k, json[k]);
            }
        },
        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

$(".chosen").chosen();
$(".chosen").chosen();