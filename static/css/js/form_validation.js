function validateLoginForm() {
    var email = document.getElementById('email');
    var password = document.getElementById('password');

    if (!email || !password || email.value.trim() === '' || password.value.trim() === '') {
        displayErrorMessage('Please enter both email and password.');
        return false;
    }

    return true;
}

function togglePasswordVisibility() {
    var passwordInput = document.getElementById('password');
    if (passwordInput) {
        passwordInput.type = (passwordInput.type === 'password') ? 'text' : 'password';
    }
}

function displayErrorMessage(message) {
    var errorMessageElement = document.getElementById('error-message');
    if (errorMessageElement) {
        errorMessageElement.innerText = message;
        errorMessageElement.style.display = 'block';
    }
}


