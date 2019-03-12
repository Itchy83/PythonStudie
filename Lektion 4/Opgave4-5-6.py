OrdbogD_E = {
    'hej': 'hello',
    'godaften': 'good evening',
    'godnat': 'goodnight',
    'badeværelse': 'bathroom',
    'køkken': 'kitchen',
    'loft': 'loft',
    'kælder': 'basement',
    }

DanskOrd = ''
EngelskOrd = ''
FlereOrd = True
DanskOk = False
EngelskOk = False
Godkendelse = False
OpslagOrdbogD_E = False

while FlereOrd:
    DanskOk = False
    EngelskOk = False
    Godkendelse = False
    Godkend = ''
    print('Indtast ord til Dansk/Engelsk - OBS:Indtast "q" for at afslutte')
    while not DanskOk:
        DanskOrd = input('Dansk:').lower()
        DanskOrdWW = DanskOrd.replace(' ', '')
        if DanskOrd == 'q':
            break
        elif DanskOrdWW.isalpha():
            DanskOk = True
        else:
            print('Ordet skal bestå af bogstaver')
    if DanskOrd == 'q':
        break
    while not EngelskOk:
        EngelskOrd = input('Engelsk:').lower()
        EngelskOrdWW = EngelskOrd.replace(' ', '')
        if EngelskOrd == 'q':
            break
        elif EngelskOrdWW.isalpha():
            EngelskOk = True
        else:
            print('Ordet skal bestå af bogstaver')
    if EngelskOrd == 'q':
        break
    while not Godkendelse:
        print('Er de indtastede ord korrekte? (j/n) - OBS:Indtast "q" for at afslutte')
        Godkend = input(':').lower()
        if Godkend == 'n':
            break
        if Godkend == 'q':
            break
        if Godkend == 'j':
            OrdbogD_E[DanskOrd] = EngelskOrd
            Godkendelse = True
        else:
            print('Indtastnings muligheder er j/n - OBS:Indtast "q" for at afslutte')
    if Godkend == 'q':
        break
while not OpslagOrdbogD_E:
    print('Hvilket dansk ord vil du gerne slå op i ordbogen?')
    OpslagD_E = input('Dansk ord:').lower()
    OpslagD_EWW = OpslagD_E.replace(' ', '')
    if OpslagD_E == 'q':
        break
    elif OpslagD_EWW.isalpha():
        print('Engelsk ord: ' + OrdbogD_E.get(OpslagD_E, 'Ordet er ikke fundet i ordbogen'))
    else:
        print('Ordet du ønsker at slå op må kun bestå af bogstaver!')

# Opgave 6

OrdbogE_D = {}
OpslagOrdbogE_D = False

for DOrd, EOrd in OrdbogD_E.items():
    OrdbogE_D[EOrd] = DOrd

while not OpslagOrdbogE_D:
    print('Hvilket engelsk ord vil du gerne slå op i ordbogen?')
    OpslagE_D = input('Engelsk ord:').lower()
    OpslagE_DWW = OpslagE_D.replace(' ', '')
    if OpslagE_D == 'q':
        break
    elif OpslagE_DWW.isalpha():
        print('Dansk ord: ' + OrdbogE_D.get(OpslagE_D, 'Ordet er ikke fundet i ordbogen'))
    else:
        print('Ordet du ønsker at slå op må kun bestå af bogstaver!')
