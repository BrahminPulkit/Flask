function validateLoginForm() {
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    if (email.trim() === '' || password.trim() === '') {
        alert('Please enter both email and password.');
        return false;
    }

    return true;
}

function togglePasswordVisibility() {
    var passwordInput = document.getElementById('password');
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
    } else {
        passwordInput.type = 'password';
    }
}

function displayErrorMessage(message) {
    var errorMessageElement = document.getElementById('error-message');
    errorMessageElement.innerText = message;
    errorMessageElement.style.display = 'block';
}

// In HTML: <div id="error-message" style="display: none;"></div>


// In HTML: <button onclick="togglePasswordVisibility()">Show/Hide Password</button>


// In HTML: <form onsubmit="return validateLoginForm()">
