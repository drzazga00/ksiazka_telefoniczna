osoby = {
    'Adam Kowalski' :{
        'imie' : 'Adam',
        'nazwisko' : ' Kowalski',
        'numer' : '123555432'
        },
    'Anna Nowak' :
    {
        'imie' : 'Anna',
        'nazwisko' : ' Nowka',
        'numer' : '506515607'
        }
}


menu = '''
MENU:
1 - Wyswietl wszystkie wpisy
2 - Stworz nowy wpis
3 - Usun wpis
4 - Wyszukaj wpis
5 - Wyjdz
---------------
'''




def wyswietl():
    for k, v in osoby.items():
        wpis = '{0:20s} --- {1:9s}'
        print(wpis.format(k.center(20),v['numer']))

def new():
    name = input('Podaj imie: ')
    sur_name = input('Podaj nazwisko: ')
    while True:
        num = input('Podaj numer telefonu: ')
        if len(num) == 9 and num.isdigit():
            break

    osoby[name.title() + ' ' + sur_name.title()] = {
        'imie' : name.title(),
        'nazwisko' : sur_name.title(),
        'numer' : num
        }

def remove():
    out = input('Podaj imie i nazwisko osoby do usuniecia: ')
    del osoby[out]
    print( '------USUNIETO------')
    print(out)


def search():
    s = input('Podaj imie lub nazwisko: ')
    znaleziono = False
    for k in osoby.keys():
        if k.find(s) != -1:
            print(osoby[k])
            znaleziono = True
            break
    if not znaleziono:
        print('brak')
            #continue
    
while True:
    print(menu)
    letter = int(input())
    if letter == 1:
        wyswietl()
        continue
    if letter == 2:
        new()
        continue
    if letter == 3:
        remove()
        continue
    if letter == 4:
        search()
        continue
    if letter == 5:
        break
