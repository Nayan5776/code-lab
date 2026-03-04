document
  .getElementsByClassName("form")
  .addEventListener("submit", function (submit) {
    submit.preventDefault();

    let Form_Validation = true;

    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();

    if (email === "@") {
      Form_Validation = true;
    }

    if (name === "") {
      Form_Validation = false;
    }

    if (Form_Validation) {
      $("#form_submit").html(
        "<span style = 'color:green'> Thank you, Your Form is Submitted."
      );
    }
  });
