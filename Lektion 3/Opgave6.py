Norden = ['danmark', 'sverige', 'norge', 'finland', 'grønland','færøerne', 'danmark']
if 'Danmark' in Norden:
    print('Ja')
else:
    print('Nej')
if 'Tyskland' in Norden:
    print('Ja')
else:
    print('Nej')

print('----------------------------------------------------------------')


Fundet = False
print('Vil ud søge hele listen eller til fundne? J/N')
Alle = input(': ').lower()
while not Fundet:
    print('Hvilket land vil du søge efter i listen?')
    Land = input(': ').lower()
    for Nord in Norden:
        if Land in Nord:
            if not Fundet:
                print('Ja i:')
            print('\t' + Nord.title())
            Fundet = True
            if Alle == 'n':
                break
    if not Fundet:
        print('Nej, desværre')
