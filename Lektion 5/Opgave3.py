

def RegneStykket(tal, starttal=0):
    for nr in tal:
        starttal = nr + starttal
    tal.append(starttal)


ListMedtal = [1, 2, 3, ]

print(ListMedtal)

Resultat = RegneStykket(ListMedtal)

print(ListMedtal)
