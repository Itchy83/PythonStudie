"""Lav en funktion som kan modtage en liste af tal og så skal den vha af return returnere summen af de tal.
 Du skal bruge en for løkke. F.eks. ved et input på [1,2,3] skal den returnere 6."""


def RegneStykket(tal, starttal=0):
    for nr in tal:
        starttal = nr + starttal
    return starttal

ListMedtal = [1, 2, 3, ]

Resultat = RegneStykket(ListMedtal)
ResultatMedStart = (RegneStykket(ListMedtal, 5))

print(Resultat)
print(ResultatMedStart)