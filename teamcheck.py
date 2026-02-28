from pyscript import document

# Function that runs when the "Check My Team" button is clicked
def check_team(e):

    # Get user inputs from the form fields
    name = document.getElementById("name").value
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value

    # Get selected radio button values for registration and medical clearance
    registration = document.querySelector('input[name="registration"]:checked')
    medical = document.querySelector('input[name="medical"]:checked')

    # Get the image element for the team logo
    img = document.getElementById("logo")

    # Hide the image by default every time button is clicked
    img.style.display = "none"

    # Store team assignments based on grade and section
    teams = {
        "7": {
            "Ruby": ("Yellow Tigers", "tigers.png"),
            "Sapphire": ("Red Bulldogs", "bulldogs.png"),
            "Emerald": ("Blue Bears", "bears.png"),
            "Topaz": ("Green Hornets", "hornets.png")
        },
        "8": {
            "Ruby": ("Red Bulldogs", "bulldogs.png"),
            "Emerald": ("Yellow Tigers", "tigers.png"),
            "Topaz": ("Blue Bears", "bears.png"),
            "Sapphire": ("Green Hornets", "hornets.png")
        },
        "9": {
            "Sapphire": ("Yellow Tigers", "tigers.png"),
            "Topaz": ("Red Bulldogs", "bulldogs.png"),
            "Ruby": ("Blue Bears", "bears.png"),
            "Emerald": ("Green Hornets", "hornets.png")
        },
        "10": {
            "Sapphire": ("Yellow Tigers", "tigers.png"),
            "Emerald": ("Red Bulldogs", "bulldogs.png"),
            "Topaz": ("Blue Bears", "bears.png"),
            "Ruby": ("Green Hornets", "hornets.png")
        }
    }

    # Check if user answered the registration question
    if registration != None:

        # Check if user answered the medical clearance question
        if medical != None:

            # Check if the user completed registration
            if registration.value == "yes":

                # Check if the user has medical clearance
                if medical.value == "yes":

                    # Check if a grade level was selected
                    if grade != "":

                        # Check if a section was selected
                        if section != "":

                            # Get the team based on grade and section
                            if grade in teams and section in teams[grade]:
                                team, logo = teams[grade][section]
                            else:
                                team = "No Team"
                                logo = ""

                            # Display the result message with student's name and team
                            document.getElementById("result").innerHTML = name + ", your team is " + team

                            # Display the team logo image
                            img.src = logo
                            img.style.display = "block"

                        else:
                            # If no section selected
                            document.getElementById("result").innerHTML = "Select a section."

                    else:
                        # If no grade selected
                        document.getElementById("result").innerHTML = "Select a grade."

                else:
                    # If medical clearance is "no"
                    document.getElementById("result").innerHTML = "You need medical clearance."

            else:
                # If registration is "no"
                document.getElementById("result").innerHTML = "You must complete online registration."

        else:
            # If medical clearance question not answered
            document.getElementById("result").innerHTML = "Answer medical clearance."

    else:
        # If registration question not answered
        document.getElementById("result").innerHTML = "Answer online registration."
