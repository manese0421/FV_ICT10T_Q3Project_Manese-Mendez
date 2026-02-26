from pyscript import document

def checkTeam():

    name = document.getElementById("name").value
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value

    registration = document.querySelector('input[name="registration"]:checked')
    medical = document.querySelector('input[name="medical"]:checked')

    if registration != None:
        if medical != None:

            if registration.value == "yes":
                if medical.value == "yes":

                    if grade != "":
                        if section != "":

                            if section == "Topaz":
                                team = "Blue Bears"
                            elif section == "Sapphire":
                                team = "Yellow Tigers"
                            elif section == "Emerald":
                                team = "Red Bulldogs"
                            elif section == "Ruby":
                                team = "Green Hornets"
                            else:
                                team = "No Team"

                            document.getElementById("teamLogo").alt = name + ", your team is " + team

                        else:
                            print("Select a section.")
                    else:
                        print("Select a grade.")

                else:
                    print("You need medical clearance.")
            else:
                print("You must complete online registration.")

        else:
            print("Answer medical clearance.")
    else:
        print("Answer online registration.")