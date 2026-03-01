from pyscript import document, display

def showPlayers(e): # when the 'show players' button is clicked, this function runs

    output = document.getElementById("playerOutput") # get the output container where the player names will be displayed

    players = [ # list of all the intrams players
        "ANDES, AKINGSON JAKE",
        "AYALA, FIL CLAREN",
        "CABRILLOS, MARTINA",
        "DAED, MARY BERNADETTE",
        "DAMONDAMON, GABRIELLE",
        "DE JESUS, MIKE JARED",
        "DERAY, JOSEPH WILSON",
        "DUMAGUING, AUDREY ANNE",
        "ECRAELA, PAULINE",
        "ESCARDA, GIOVANNI",
        "FABUL, ZION MARGARET",
        "FERRER, MARGAUX ALAINA",
        "GOROM, VICTOR CARLO",
        "GRANDE, NATHAN MARI",
        "LIGAS, JOHN VINCENT",
        "MANESE, MARLEY SUMMER",
        "MENDEZ, CYRENNE GRACE",
        "NOBLE, DANIELLE ALEENA",
        "SALAPUNEN, RISO",
        "SANTOS, ASHLEY KIRSTEN",
        "TACAN, ALEXANDER",
        "JR. TARUC, JOHN ALFRED",
        "TENORIO, KURT GABRIEL",
        "TIONGSON, NATHANIEL",
        "UBANA, AURORA ISHTAR",
        "VILLANUEVA, ALEXI AVIOLE",
        "ZALES, JARIX JOHNUAY"
    ]

    output.innerHTML = "" # clears the previous input so results dont duplicate

    for i, p in enumerate(players, start=1): # loop through the list of players and displays them numbered

        if "," in p: # checks if the player string includes a comma, as per the format
            parts = p.split(",") # splits the string: last name, first name

        if len(parts) == 2: # if the split produces exactky 2 parts:

            # remove extra spaces and assign last name and first name
            lastname = parts[0].strip()
            firstname = parts[1].strip()

            # display the formatted player name with numbering
            output.innerHTML += f"{i}) {lastname}, {firstname}<br>"

