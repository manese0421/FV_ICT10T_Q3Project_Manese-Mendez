from pyscript import document, display

def sign_up(event):

    username = document.getElementById("user").value
    password = document.getElementById("pass").value
    output = document.getElementById("output")

    messages = []

    if len(username) <= 7:
        missing_user = 7 - len(username)
        messages.append(f"Username needs {missing_user} more character(s).")
 
    if len(password) < 10:
        missing_pass = 10 - len(password)
        messages.append(f"Password needs {missing_pass} more character(s).")

    if not any(char.isalpha() for char in password):
        messages.append("Password needs at least 1 letter.")

    if not any(char.isdigit() for char in password):
        messages.append("Password needs at least 1 number.")

    if messages:
        output.innerHTML = "<br>".join(messages)
    else:
        output.innerText = "Account created successfully!"
