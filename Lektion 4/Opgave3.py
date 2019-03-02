# Opgave 3 En pakkeliste via user input

Kuffert = []
AntalKuffert = 0
AntalLigTal = False
AntalGenstande = 0

while not AntalLigTal:
    print('Hvor mange genstande skal pakkes til rejsen?')
    AntalGenstande = input(': ')
    if AntalGenstande.isdigit():
        AntalLigTal = True
        break
    else:
        print('Antal må kun bestå af tal')


while len(Kuffert) < int(AntalGenstande):
    print('Hvad skal i kufferten? OBS: Tryk "q" for at stoppe')
    if len(Kuffert) != 0:
        print('Du har stadig plads til ' + str(int(AntalGenstande) - len(Kuffert)) + ' ting i kufferten')
    Genstand = input(': ').lower()
    if Genstand == 'q':
        print('Du valgte at stoppe din kuffertpak')
        break
    elif Genstand == '':
        print('Du kan ikke putte ingenting i kufferten')
    else:
        Kuffert.append(Genstand)

print('\nDit kufferindhold består af:')
for GenstandKuffert in Kuffert:
    print('\t' + GenstandKuffert.title())
