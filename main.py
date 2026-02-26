from pyscript import document

def sign_up():

    username = document.getElementById("user").value
    password = document.getElementById("pass").value
    output = document.getElementById("output")

    if len(username) >= 7:

        has_letter = False
        has_number = False

        for char in password:
            if char.isalpha():
                has_letter = True
            elif char.isdigit():
                has_number = True

        if len(password) >= 10:
            if has_letter:
                if has_number:
                    output.innerText = "Account successfully created!"
                else:
                    output.innerText = "Password must contain a number."
            else:
                output.innerText = "Password must contain a letter."
        else:
            output.innerText = "Password must be at least 10 characters long."

    else:
        output.innerText = "Username must be at least 7 characters long."