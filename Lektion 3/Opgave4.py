# Opgave 4 - tilføjelse og sletning af key/values

# Dictionarie fra opgave 2:
Personer = {
    'allan': 'jensen',
    'jeppe': 'bjerregaard',
    'henrik': 'madsen',
    'finn': 'jensen',
    'christian': 'høgh',
    }

print(Personer)

Personer['bjarne'] = 'jensen'

print(Personer)

Personer.update({
    'kaare': 'ravn',
    'christian': 'lønbæk'})  # På den her måde kan der tilføjes flere elementer


for Navn, Efternavn in Personer.items():
    print('\nFornavn: ' + Navn.title())
    print('Efternavn: ' + Efternavn.title())


del Personer['allan']

print('\nListe efter position 1 er slettet')
for Navn, Efternavn in Personer.items():
    print('\nFornavn: ' + Navn.title())
    print('Efternavn: ' + Efternavn.title())

print(Personer.get('jeppe', 'findes ikke!'))  #Kan bruges så program ikke crasher, findes ikke! printes hvis det ikke findes



