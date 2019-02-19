# OPGAVE 5-1 FRA BOGEN SIDE 82

LommeIndhold = 'Nøgler'

print('Har jeg nøgler i lommen?')
print(LommeIndhold == 'Nøgler')     # Dette udtryk er sandt, derfor kvitteres der med TRUE

print('Har jeg en telefon i lommen?')
print(LommeIndhold == 'Telefon')    # Dette udtryk er falsk, derfor kvitteres der med FALSE

print('\n')
'''-------------------------------------------------------------------------------------------'''
Taskeindhold = ['kuglepen', 'post it', 'pung', 'smøger', 'nøgler', 'tyggegummi', 'marsbar']

if 'kuglepen' and 'post it' in Taskeindhold:
    print('JA')
else:
    print('NEJ')

print('\n')
'''-------------------------------------------------------------------------------------------'''
KlarTilByen = ['pung', 'smøger', 'nøgler', 'tyggegummi']

if KlarTilByen in Taskeindhold:
    print('Ud af døren!!')
else:
    print('Du har ikke det hele med!!')

print('\n')
'''-------------------------------------------------------------------------------------------'''
