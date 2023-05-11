$(document).ready(() => {
  var $msg_input = $("#msg_input");
  var $chatlist = $("#chatlist");
  var $chatform = $("#chatform");
  var $username = localStorage.getItem("username");

  var SERVER_URL = "http://localhost:5000";

  const sendMessage = (isMe) => {
    var message = $msg_input.val();
    var data = {
      username: $username,
      message: message,
    };

    $.ajax({
      url: SERVER_URL + "/api/message",
      method: "POST",
      contentType: "application/json",
      data: JSON.stringify(data),
      success: (data) => {
        $chatlist.append($("<li class='userInput'>").text(data.message));
        $msg_input.val("");
        $chatlist.scrollTop($chatlist[0].scrollHeight);
      },
      error: (xhr, status, error) => {
        console.error("Erreur AJAX : " + status + " - " + error);
        alert("ERRUR");
      },
    });
  };

  // Lorsqu'on envoi un message
  $chatform.on("submit", (event) => {
    event.preventDefault();
    sendMessage(true);
  });

  // Lorsque la page est chargée completement
  $(window).on("load", function () {
    getAllMessage();
  });

  setInterval(() => {
    getAllMessage();
  }, 20000);

  // Fonction qui doit recuperer les messages (tout)
  const getAllMessage = () => {
    $.ajax({
      url: SERVER_URL + "/api/messages",
      method: "GET",
      contentType: "application/json",
      success: (data) => {
        $.each(data, (index, message) => {
          if (message.username == $username) {
            $chatlist.append($("<li class='userInput'>").text(message.message));
          } else {
            $chatlist.append(
              $("<li class='bot__output bot__output--standard'>").text(
                message.message
              )
            );
          }
          $chatlist.scrollTop($chatlist[0].scrollHeight);
        });
      },
      error: (xhr, status, error) => {
        console.error("Erreur AJAX : " + status + " - " + error);
        alert("ERRUR");
      },
    });
  };
});
