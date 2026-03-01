from pyscript import document, display

def sign_up(event): # function runs when the sign up button is clicked

    username = document.getElementById("user").value # gets the value entered in the username input field

    password = document.getElementById("pass").value # gets the value entered in the password input field

    output = document.getElementById("output") # gets the output div where messages will be displayed

    messages = [] # empty list to store error messages

    if len(username) <= 7: # checks if username length is 7 characters or less
        missing_user = 7 - len(username) # calculate how many more characters are needed

        messages.append(f"Username needs {missing_user} more character(s).") # add message to the list
 
    if len(password) < 10: # checks if password is less than 10 characters
        missing_pass = 10 - len(password) # calculate missing characters

        messages.append(f"Password needs {missing_pass} more character(s).") # add message to the list

    if not any(char.isalpha() for char in password): # checks if password contains at least one letter
        messages.append("Password needs at least 1 letter.")

    if not any(char.isdigit() for char in password): # checks if password contains at least one number
        messages.append("Password needs at least 1 number.")

    if messages: # if there are any error messages, display them
        output.innerHTML = "<br>".join(messages) # join messages with line breaks and display them in the output box
    else:
        output.innerText = "Account created successfully!" # if no errors, show success message

