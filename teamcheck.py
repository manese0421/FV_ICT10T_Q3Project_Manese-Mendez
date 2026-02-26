from pyscript import document

def check_team(e):

    name = document.getElementById("name").value
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value

    registration = document.querySelector('input[name="registration"]:checked')
    medical = document.querySelector('input[name="medical"]:checked')

    # default hide image
    img = document.getElementById("logo")
    img.style.display = "none"

    if registration != None:
        if medical != None:

            if registration.value == "yes":
                if medical.value == "yes":

                    if grade != "":
                        if section != "":

                            if section == "Topaz":
                                team = "Blue Bears"
                                logo = "bears.png"

                            elif section == "Sapphire":
                                team = "Yellow Tigers"
                                logo = "tigers.png"

                            elif section == "Emerald":
                                team = "Red Bulldogs"
                                logo = "bulldogs.png"

                            elif section == "Ruby":
                                team = "Green Hornets"
                                logo = "hornets.png"

                            else:
                                team = "No Team"
                                logo = ""

                            # show result text
                            document.getElementById("result").innerHTML = name + ", your team is " + team

                            # show image
                            img.src = logo
                            img.style.display = "block"

                        else:
                            document.getElementById("result").innerHTML = "Select a section."
                    else:
                        document.getElementById("result").innerHTML = "Select a grade."

                else:
                    document.getElementById("result").innerHTML = "You need medical clearance."
            else:
                document.getElementById("result").innerHTML = "You must complete online registration."

        else:
            document.getElementById("result").innerHTML = "Answer medical clearance."
    else:
        document.getElementById("result").innerHTML = "Answer online registration."