const form = document.getElementById('form');
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('confirm-password');

form.addEventListener('submit', (event) => {

    checkInputs();

    if(isFormValid()==true){
        form.submit();
    }else {
        event.preventDefault();
    }
     
});

function isFormValid(){
    const inputContainer = form.querySelectorAll(".form-control");
    let result=true;
    inputContainer.forEach((container)=>{
        if(container.classList.contains('error')){
            result=false;
        }
    });

    return result;
}

function checkInputs() {

    if(username.value.trim() == '') {
        setErrorFor(username, 'Username cannot be blank');
       
    } else {
          setSuccessFor(username);
    }

    if(email.value.trim() == '') {
        setErrorFor(email, 'Email cannot be blank');
    } else if(isEmailValid(email.value)) {
        setSuccessFor(email)
    } else {
        setErrorFor(email, 'Provide valid email');
    }

    if(password.value.trim() == '') {
        setErrorFor(password, 'Password cannot be blank');
    } else {
        setSuccessFor(password);
    }

    if(password2.value.trim() == '') {
        setErrorFor(password2, 'Confirm-password cannot be blank')
    } else if(password.value.trim() !== password2.value.trim()) {
        setErrorFor(password2, 'Passwords does not match');
    } else {
        setSuccessFor(password2);
    }
}

function setErrorFor(element, message) {
    const parent = element.parentElement;
    if(parent.classList.contains('success')){
        parent.classList.remove('success');
    }
    parent.classList.add("error");
    const paragraph = parent.querySelector('p');
    paragraph.textContent = message;
}

function setSuccessFor(element) {
    const parent = element.parentElement;
    if(parent.classList.contains('error')){
        parent.classList.remove('error');
    }
    parent.classList.add("success")

   
}

function isEmailValid(email) {
    const reg =  /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return reg.test(email);
}

