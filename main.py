from pyscript import document, display

# Function that runs when the Sign Up button is clicked
def sign_up(event):

    # Get the value entered in the username input field
    username = document.getElementById("user").value

    # Get the value entered in the password input field
    password = document.getElementById("pass").value

    # Get the output div where messages will be displayed
    output = document.getElementById("output")

    # Create an empty list to store error messages
    messages = []

    # Check if username length is 7 characters or less
    if len(username) <= 7:
        # Calculate how many more characters are needed
        missing_user = 7 - len(username)

        # Add message to the list
        messages.append(f"Username needs {missing_user} more character(s).")
 
    # Check if password is less than 10 characters
    if len(password) < 10:
        # Calculate missing characters
        missing_pass = 10 - len(password)

        # Add message to the list
        messages.append(f"Password needs {missing_pass} more character(s).")

    # Check if password contains at least one letter
    if not any(char.isalpha() for char in password):
        messages.append("Password needs at least 1 letter.")

    # Check if password contains at least one number
    if not any(char.isdigit() for char in password):
        messages.append("Password needs at least 1 number.")

    # If there are any error messages, display them
    if messages:
        # Join messages with line breaks and display them in the output box
        output.innerHTML = "<br>".join(messages)
    else:
        # If no errors, show success message
        output.innerText = "Account created successfully!"
