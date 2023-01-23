// Variables for email and <p> error element
const emailInput = document.getElementById("email");
const emailJavascript = document.getElementById("email-javascript");

function setErrorFor(element, message) {
    element.classList.remove("success");
    element.classList.add("error");
    element.innerHTML = message;
} 

function setSuccesFor(element, message) {
    element.classList.remove("error");
    element.classList.add("success");
    element.innerHTML = message;
} 

emailInput.addEventListener("input", function(){
  let emailValue = emailInput.value;
  let emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

  if(!emailPattern.test(emailValue)) {
    setErrorFor(emailJavascript, "The email format is invalid");
  } else {
    setSuccesFor(emailJavascript, "The email format is valid");
  }
});      

