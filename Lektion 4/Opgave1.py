# Opgave 7-1 side 121 i bogen

print('Hvilken bil kunne I tænke jer at leje?')
Bil = input(': ')
print("Lad med lige kigge i pc'eren om vi har en " + Bil + ' ledig')

"""----------------------------------------------------------"""

# Opgave 7-2 side 121 i bogen

Antal = int(input('Hvor mange er skal I have bord til?: '))
if Antal <= 8:
    print('Følg med mig, så viser jeg jer ned til jeres bord')
if Antal > 8:
    print('Desværre')

"""----------------------------------------------------------"""

# Opgave 7-3 side 121 i bogen

print('Kan det her nummer gå op i 10?')
Tal = int(input(': '))

if Tal % 10 == 0 and Tal != 0:
    print('Ja')
else:
    print('Nej')

"""----------------------------------------------------------"""
