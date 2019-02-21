# Opgave 5 - nesting.

Tyskland = {'Land': 'tyskland', 'Byer': ['berlin', 'hamborg', 'münchen']}
England = {'Land': 'england', 'Byer': ['london', 'birmingham', 'glasgow']}
Frankrig = {'Land': 'frankrig', 'Byer': ['Paris', 'marseille', 'lyon']}

print(Tyskland['Land'].title())
for By in Tyskland['Byer']:
    print('\t' + By.title())


print(England['Land'].title())
for By in England['Byer']:
    print('\t' + By.title())


print(Frankrig['Land'].title())
for By in Frankrig['Byer']:
    print('\t' + By.title())


Ungarn = {'Land': 'ungarn', 'Byer': ['budapest', 'debrecen', 'szeged']}

Contries = [Tyskland, England, Frankrig, Ungarn]

for Contrie in Contries:
    print("\n" + Contrie['Land'].title())
    for By in Contrie['Byer']:
        print('\t' + By.title())


Sverige = {'Stockholm', 'Götheborg', 'Malmø'}
Danmark = {'Købenavn', 'Århus', 'Odense'}
Norge = {'Oslo', 'Bergen', 'Trondheim'}

Norden = [Sverige, Danmark, Norge]



