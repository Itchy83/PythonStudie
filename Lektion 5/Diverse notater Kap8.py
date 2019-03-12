def HelloWorld():                      # simpel defination
    """ Her er det en god ide at beskrive hvad funktionen gør"""
    print('Hello World')

HelloWorld()               #Køres ved bare at skrive navnet på den.

print('----------------------------------------------------------------------------------')


def hej(navn):
    """Det her en en def med input, i det her tilfælde et navn"""
    print('Hej, ' + navn + '! Hvordan har du det?')

hej('Mille-My')
hej('Bjarne')

print('----------------------------------------------------------------------------------')

def MinBil(brand, variation):
    """ Her er det brugt to input i defination """
    print('\nMin bil er en ' + brand + '!')
    print('Min ' + brand + ' er en model ' + variation + '!')

MinBil('Fiat', 'Panda')

print('----------------------------------------------------------------------------------')

def dyr(navn, slags='Hund'):    # I definatinon defineres, hvis intet bliver nævnt når man kalder def, hund er "Default"
    """I den her defination eksempel, prøver kun at nævn en af tingene"""
    print('\nNaboens dyr er en ' + slags + '!')
    print('Deres ' + slags + ' hedder ' + navn + '!')

dyr(navn='Bailey')

print('----------------------------------------------------------------------------------')

