# Opgave 5 - nesting.

Lande = {
    'Tyskland' : ['berlin', 'hamborg', 'münchen'],
    'England' : ['london', 'birmingham', 'glasgow'],
    'Frankrig' : ['Paris', 'marseille', 'lyon'],
    }

for Land, Byer in Lande.items():
    print(Land.title() + ':')
    for By in Byer:
        print("\t" + By.title())

Sverige = {'Stockholm', 'Götheborg', 'Malmø'}
Danmark = {'Købenavn', 'Århus', 'Odense'}
Norge = {'Oslo', 'Bergen', 'Trondheim'}

Norden = [Sverige, Danmark, Norge]
print(Norden)

for NLand in Norden.items():
    print(NLand)
    for NBy in NLand:
        print(NBy)
