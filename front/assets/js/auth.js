$(document).ready(() => {
  $(window).on("load", () => {
    let $username = localStorage.getItem("username");

    if ($username) {
      $(location).prop("href", "/chat.html");
    }
  });

  var $username = $("#username");
  var $login_form = $("#login-form");
  var SERVER_URL = "http://localhost:5000";

  $login_form.on("submit", (event) => {
    event.preventDefault();

    var data = {
      username: $username.val(),
    };

    $.ajax({
      url: SERVER_URL + "/api/users",
      method: "POST",
      contentType: "application/json",
      data: JSON.stringify(data),
      success: (data) => {
        localStorage.setItem("username", data.username);
        $(location).prop("href", "chat.html");
      },
      error: (xhr, status, error) => {
        console.error("Erreur AJAX : " + status + " - " + error);
        alert("ERRUR");
      },
    });
  });
});
