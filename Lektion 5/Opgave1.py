# Opgave 1
# 8-3 fra bogen

def kluns(size, slogan):
    print('Du har bestilt en størrelse ' + size +', med sloganet "' + slogan +'"')


kluns('large', 'Mega Fedt!')

kluns(slogan='Anel', size='Ekstra Small')

# 8-3 fra bogen


def by_beskrivelse(by, land='Danmark'):
    print(str(by).title() + ' er en by i ' + land)


by_beskrivelse('Horsens')
by_beskrivelse('Berlin', 'Tyskland')
by_beskrivelse('Randers')

