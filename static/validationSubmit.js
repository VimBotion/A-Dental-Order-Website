const form = document.getElementById("form")
const username = document.getElementById("username")
const email = document.getElementById("email")
const password = document.getElementById("password")
const passwordConfirmation = document.getElementById("confirm-password")

form.addEventListener("submit", e => {
    e.preventDefault();

    validateInputs();
});

const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add("error");
    inputControl.classList.remove("success");
}

const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add("success");
    inputControl.classList.remove("error");
};

const isValidEmail = email => {
    let emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    return emailPattern.test(String(email).toLowerCase());
}

const validateInputs = () => {
    const usernameValue = username.value.trim();
    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();
    const passwordConfirmationValue = passwordConfirmation.value.trim();

    if(usernameValue === "") {
        setError(username, "Username is required");
    } else {
        setSuccess(username);
    }

    if(emailValue === "") {
        setError(email, "Email is required");
    } else if (!isValidEmail(emailValue)){
        setError(email, "Provide a valid email addres");
    } else {
        setSuccess(email);
    }

    if(passwordValue === "") {
        setError(password, "Password is required");
    } else {
        setSuccess(password);
    } 

    if(passwordConfirmationValue === "") {
        setError(passwordConfirmation, "Please confirm your password");
    } else if (passwordConfirmationValue !== passwordValue) {
        setError(passwordConfirmation, "Passwords doesn't match");
    } else {
        setSuccess(passwordConfirmation)
    }
} 
