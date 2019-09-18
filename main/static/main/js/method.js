$(function() {
  $("#html-output").html(
    "<p style='color: gray'>Output will be shown here</p>"
  );
  $("#save").click(function(e) {
    var code = editor.getValue();
    $("#html-output").html(code);
    var currentdate = new Date();
    var datetime =
      currentdate.getDate() +
      "/" +
      (currentdate.getMonth() + 1) +
      "/" +
      currentdate.getFullYear() +
      " @ " +
      currentdate.getHours() +
      ":" +
      currentdate.getMinutes() +
      ":" +
      currentdate.getSeconds();
    $.ajax({
      url: "/save_to_db/",
      data: { code: code, datetime: datetime, csrfmiddlewaretoken: csrftoken },
      type: "POST"
    }).done(function(response) {
      alert(response);
    });
  });
});
