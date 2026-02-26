from pyscript import document

def showPlayers():

    output = document.getElementById("playerOutput")

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

    output.innerHTML = ""

    for p in players:

        if "," in p:
            parts = p.split(",")

            if len(parts) == 2:
                lastname = parts[0]
                firstname = parts[1]

                if lastname != "" and firstname != "":
                    output.innerHTML += lastname + ", " + firstname + "<br>"