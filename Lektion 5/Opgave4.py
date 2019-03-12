''' Lav en funktion “borrow_books” som kan tage et vilkårligt antal strings som input -
altså titler på bøger. Funktionen skal så skrive ud hvor mange bøger der bliver angivet som parametre
(husk at parametrene i dette tilfælde kommer ind i funktionen som en liste) samt alle titlerne (med en for loop)
 '''


def borrow_comics(*books):
    print('Antal lånte tegneserier er: ' + str(len(books)) + '\n')
    for book in books:
        print(book)


borrow_comics('Lucky Look', 'Anders And', 'TinTin', 'Steen & Stoffer')

