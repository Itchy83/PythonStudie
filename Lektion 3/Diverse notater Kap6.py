
Listen = ['Christian', 'Finn', 'Lars', 'Jeppe', 'Henrik']

again = True
againv2 = False

while again == True:
    print('Er vedkomne i gæstelisten')
    Person = input(": ")
    if Person in Listen:
        print('Ja')
    elif Person not in Listen:
        print('Nej')
while againv2 == False:
        Igen = input("Vil du spørge om flere? J/N: ")
    if Igen == "J":
        again = True
    elif Igen == "N":
        again = False
    elif Igen != "J" or "N":
        print('Kommando ikke forstået')
        againv2 = False
