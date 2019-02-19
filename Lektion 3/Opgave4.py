# Opgave 4 - tilføjelse og sletning af key/values

# Dictionarie fra opgave 2:
Personer = {
    'allan': 'jensen',
    'jeppe': 'bjerregaard',
    'henrik': 'madsen',
    'finn': 'jensen',
    'christian': 'høgh',
    }

Personer['kaare'] = 'ravn'

Personer.update({'kaare': 'ravn'})


for Navn, Efternavn in Personer.items():
    print('\nFornavn: ' + Navn.title())
    print('Efternavn: ' + Efternavn.title())


del Personer['allan']

print('\nListe efter position 1 er slettet')
for Navn, Efternavn in Personer.items():
    print('\nFornavn: ' + Navn.title())
    print('Efternavn: ' + Efternavn.title())


