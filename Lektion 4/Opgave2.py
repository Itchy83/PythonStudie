# Opgave 7-5 side 121 i bogen


Entre = True
Total = 0
Igen = False

print('Velkommen til MegaScope!')
while Entre:
    Flere = ''
    Alder = int(input('Hvor gammel er du? '))
    if Alder < 3:
        print('Du har gratis entre!')
    elif 3 <= Alder <= 12:
        print('Entre koster 100kr')
        Total += 100
    elif Alder > 12:
        print('Entre koster 120kr')
        Total += 120
    Igen = True
    while Igen:
        Flere = input('Er I flere som skal i bio? (j/n)')
        if Flere == 'n':
            Entre = False
            break
        elif Flere == 'j':
            Igen = False
        else:
            print('Indtastning ikke forstået')



print('Det bliver i alt ' + str(Total) + ('kr.'))
