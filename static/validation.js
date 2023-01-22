const emailInput = document.getElementById("email");
const feedback = document.getElementById("feedback");
const sumitBtn = document.getElementById("submit")

function setErrorFor(element, message) {
      element.classList.remove("succes");
      feedback.classList.add("error");
      feedback.innerHTML = message;
} 

function setSuccesFor(element, message) {
      element.classList.add("succes");
      feedback.innerHTML = message;
} 

emailInput.addEventListener("input", function(){
  let email = emailInput.value;
  let emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

  if(!emailPattern.test(email)) {
    setErrorFor(feedback, "The email format is invalid")
  } else {
    setSuccesFor(feedback, "The email format is valid")
  }
});
