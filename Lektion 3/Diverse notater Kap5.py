
Kollegaer = ['Christian', 'Jeppe', 'Henrik', 'Peter', 'Simon']
Tom = []
Fyldt = [':-)']

for Kollega in Kollegaer:
    if Kollega == 'Henrik':
        Tom = Fyldt
        print(Kollega.upper())
    else:
        print(Kollega.lower())
print(Tom)



Mc = 'Yamaha'
Mc == 'Yamaha'      # Men 2 ligmed, spørger man om Mc virkelig er lig med Yamaha, i det her tilfælde! Case sensitive

Bil = 'Toyota'
Bil.lower() == 'toyota'  # Lower kan bruges til at lave en case insensitive


Frugt = 'drue'

if Frugt != 'banan':    # Et udråbtegn for at ligmed != Betyder ikke ligmed
    print('OK')


'''--------------------------------------------------------------------------------------'''

Allan = 35
Peter = 40
Jeppe = 50
Krav = 30


if (Allan or Peter or Jeppe) < Krav:       # Mindre end, større end, lig med, ikke lig med ( < > = != )
    print('\nNo Access')                   # kan alle bruges som betingelser
else:
    print('\nAccess Granted')


if Allan and Peter and Jeppe < Krav:
    print('\nNo Access')
else:

    print('\nAccess Granted')
'''--------------------------------------------------------------------------------------'''

if 'Lars' in Kollegaer:
    print('Ja, det er han')         # Her kigges efter om der er en specifik variabel i en liste.
else:
    print('Nej, det er han ikke ')

Festliste = ['Finn', 'Henrik', 'Lars', 'Christian', 'Jeppe']
Inviteret = 'Henrik'

if Inviteret in Festliste:
    print('Ja, han er inviteret!')


'''------------------------------------------------------------------------------------------------------------'''

Onsdag = True

if Onsdag:
    print('YES')
else:
    print('NO')
