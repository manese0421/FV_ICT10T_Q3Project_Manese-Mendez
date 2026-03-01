from pyscript import document

def check_team(e): # runs when the 'check my team' button is clicked

    # collects all user inputs from the form fields
    name = document.getElementById("name").value
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value

    # get selected radio button values for registration and medical clearance
    registration = document.querySelector('input[name="registration"]:checked')
    medical = document.querySelector('input[name="medical"]:checked')

    # gets the image element for the team logo
    img = document.getElementById("logo")

    # the image is hidden by default each time the button is clicked
    img.style.display = "none"

    # store team assignments based on grade and section
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

    # check if user answered the registration question
    if registration != None:

        # check if user answered the medical clearance question
        if medical != None:

            # check if the user completed registration
            if registration.value == "yes":

                # check if the user has medical clearance
                if medical.value == "yes":

                    # check if a grade level was selected
                    if grade != "":

                        # check if a section was selected
                        if section != "":

                            # get the team based on grade and section
                            if grade in teams and section in teams[grade]:
                                team, logo = teams[grade][section]
                            else:
                                team = "No Team"
                                logo = ""

                            # displays the result message with student's name and team
                            document.getElementById("result").innerHTML = name + ", your team is " + team

                            # display the team logo image
                            img.src = logo
                            img.style.display = "block"

                        else:
                            # if no section selected
                            document.getElementById("result").innerHTML = "Select a section."

                    else:
                        # if no grade selected
                        document.getElementById("result").innerHTML = "Select a grade."

                else:
                    # if medical clearance is "no"
                    document.getElementById("result").innerHTML = "You need medical clearance."

            else:
                # if registration is "no"
                document.getElementById("result").innerHTML = "You must complete online registration."

        else:
            # if medical clearance question not answered
            document.getElementById("result").innerHTML = "Answer medical clearance."

    else:
        # if registration question not answered
        document.getElementById("result").innerHTML = "Answer online registration."

