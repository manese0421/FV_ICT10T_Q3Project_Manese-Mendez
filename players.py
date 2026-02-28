from pyscript import document, display

# Function that runs when the "Show Players" button is clicked
def showPlayers(e):

    # Get the output container where player names will be displayed
    output = document.getElementById("playerOutput")

    # List of all intramural players (Last Name, First Name format)
    players = [
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

    # Clear previous output so the list doesn't duplicate every click
    output.innerHTML = ""

    # Loop through the list of players and display them with numbering
    for i, p in enumerate(players, start=1):

        # Check if the player string contains a comma (expected format)
        if "," in p:
            # Split the string into last name and first name
            parts = p.split(",")

        # If the split produced exactly 2 parts (valid format)
        if len(parts) == 2:

            # Remove extra spaces and assign last name and first name
            lastname = parts[0].strip()
            firstname = parts[1].strip()

            # Display the formatted player name with numbering
            output.innerHTML += f"{i}) {lastname}, {firstname}<br>"
