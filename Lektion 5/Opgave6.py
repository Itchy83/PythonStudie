ToMuch = '     H    E    Y    '
Stripped = ToMuch.strip(' ')
print(Stripped)

Replaced = ToMuch.replace(' ', '')
print(Replaced)

Indtastning = input('Er det her et tal: ')
if Indtastning.isdigit():
    print('Ja')
else:
    print('Nej')


FedeUdtryk = ['Blæret', 'MegaSyret', 'Flippet']
List = '#'.join(FedeUdtryk)
print(List)
print('Input skal være strings')
