

def borrow_comics(*books):
    print('Antal lånte tegneserier er: ' + str(len(books)) + '\n')
    for book in books:
        print(book)


def RegneStykket(tal, starttal=0):
    for nr in tal:
        starttal = nr + starttal
    return starttal

