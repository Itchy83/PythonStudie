# Opgave 3 - for loops og dictionaries:

# Dictionarie fra opgave 2:
Personer = {
    'allan': 'jensen',
    'jeppe': 'bjerregaard',
    'henrik': 'madsen',
    'finn': 'jensen',
    'christian': 'høgh',
    }

# loop 1: skal udskrive både keys og values og udskrive begge to

print('---------------LOOP 1--------------')
for Navn, Efternavn in Personer.items():
    print('\nFornavn: ' + Navn.title())
    print('Efternavn: ' + Efternavn.title())

# loop 2: skal kun gå igennem keys og udskrive dem

print('---------------LOOP 2--------------')
for Navn in Personer.keys():
    print('\nFornavn: ' + Navn.title())

# loop 2: sorted
print('---------------LOOP 2 V2--------------')
for Navn in sorted(Personer.keys()):
    print('\nFornavn: ' + Navn.title())

# loop2: .keys behøves ikke
print('---------------LOOP 2 V3--------------')
for Navn in Personer:
    print('\nFornavn: ' + Navn.title())


# loop 3: skal kun gå igennem values og udskrive dem.

print('---------------LOOP 3--------------')
for Navn in Personer.values():
    print('\nFornavn: ' + Navn.title())

# loop 3: sorted

print('---------------LOOP 3--------------')
for Navn in sorted(Personer.values()):
    print('\nFornavn: ' + Navn.title())
