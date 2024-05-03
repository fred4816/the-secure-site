const ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
const NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
const SPECIAL_CHARACTERS = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "\\", ":", ";", "<", ",", ">", ".", "?", "/"];
const UPPERCASE = []
for (let i = 0; i < ALPHABET.length; i++) {
    UPPERCASE.push(ALPHABET[i].toUpperCase())
}


function generatePassword (length, uppercase, special, numbers) {
    var new_password = ''
    options = [ALPHABET]

    if (numbers) {
        options.push(NUMBERS)
    }
    if (special) {
        options.push(SPECIAL_CHARACTERS)
    }
    if (uppercase) {
        options.push(UPPERCASE)
    }

    for (let i = 0; i < length; i++) {
        chosen_options = options[Math.floor(Math.random() * options.length)]
        new_password += chosen_options[Math.floor(Math.random() * chosen_options.length)]
    }

    return new_password
}


document.addEventListener('DOMContentLoaded', function() {
    let refresh_button = document.getElementById('refreshPassword');
    let special_characters_checkbox = document.getElementById('includeSpecialCharacters');
    let numbers_checkbox = document.getElementById('includeNumbers');
    let uppercase_checkbox = document.getElementById('includeUppercaseLetters');
    let password_textbox = document.getElementById('thePassword')
    let password_length_slider = document.getElementById('passwordLength');

    let include_special_characters = true;
    let include_numbers = true;
    let include_uppercase = true;
    let password_length = 16;


    function updatePassword() {
        password_textbox.value = generatePassword(password_length, include_uppercase, include_special_characters, include_numbers);
    }

    updatePassword()

    refresh_button.addEventListener('click', () => {
        updatePassword();
    });

    special_characters_checkbox.addEventListener('change', () => {
        include_special_characters = !include_special_characters;
        updatePassword();
    });

    numbers_checkbox.addEventListener('change', () => {
        include_numbers = !include_numbers;
        updatePassword();
    });

    uppercase_checkbox.addEventListener('change', () => {
        include_uppercase = !include_uppercase;
        updatePassword();
    });

    password_length_slider.oninput = function () {
        password_length = password_length_slider.value;
        document.getElementById('passwordLengthLabel').innerHTML = password_length;
        updatePassword();
    };

    document.getElementById('copyPassword').addEventListener('click', () => {
        password_textbox.select();
        navigator.clipboard.writeText(password_textbox.value);
        window.getSelection().removeAllRanges();
    })

});



