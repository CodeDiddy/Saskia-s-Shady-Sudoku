import urllib.request, json

# lees de sudoku in een variabele
url = "https://community-challenge.netlify.app/data/sudoku.json"
response = urllib.request.urlopen(url)

sudoku_json = (json.loads(response.read()))

# sla de rijen (lists) uit de sudoku op in een variabele voor de werkbaarheid
sudoku = sudoku_json['sudoku']

# print de ingevulde sudoku
def print_sudoku(check_sudoku):
    print('')
    print('*' * 10, end='')
    print(' SUDOKU ', end='')
    print('*' * 11)
    for row in check_sudoku:
        print('*', end='')
        print(row, end='')
        print('*')
    print('*' * 29)
    print('')

# * Controleer of alle rijen kloppen, horizontaal en verticaal. De input vind je in sudoku.json.

# elke rij, kolom, 3x3 en diagonaal moet 1 keer een getal vanaf 1 t/m 9 staan. Hiervoor gebruik ik een set 
doel = {1, 2, 3, 4, 5, 6, 7, 8, 9}


# help functie om de rijen te checken
def check_rij(check_sudoku, doel):
    """
    input: een lijst van lijsten met cijfers (sudoku) en een set met de gewenste cijfers voor de evaluatie
    functie controleert of er genoeg rijen in de sudoku zitten
    functie controleert of cijfers in een rij niet 2 keer voorkomen en of alle cijfers voorkomen
    output: boolean
    """
    print('Rijen aan het checken...')
    if len(check_sudoku) != 9:
        print(f"Sudoku heeft {len(check_sudoku)} rijen.")
        print('De sudoku is niet volledig ingevuld!')
        return False
    for list in check_sudoku:
        if (set(list) != doel):
            print('List is niet gelijk aan doel')
            print(set(list), " != ", doel)
            print('De rijen zijn onjuist ingevuld!')
            return False
    print('Rijen kloppen')
    return True


# help functie om de kolommen te checken
def check_kolom(check_sudoku, doel):
    """
    input: een lijst van lijsten met cijfers (sudoku) en een set met de gewenste cijfers voor de evaluatie
    functie controleert of cijfers in een kolom niet 2 keer voorkomen en of alle cijfers voorkomen
    functie moet na 'check_rij' worden aangeroepen, omdat daar de controle op aantal rijen en kolommen plaatsvindt
    output: boolean
    """
    print('Kolommen aan het checken...')
    for i in range(9):
        kolom = []
        for j in range(9):
            kolom.append(check_sudoku[j][i])
        if set(kolom) != doel:
            print('De kolommen zijn onjuist ingevuld!')
            return False
    print('Kolommen kloppen')
    return True

# ** Controleer nu ook of de "hokjes" van 3x3 kloppen.

# help functie om de blokken (3x3) te checken
def check_square(check_sudoku, doel):
    """
    input: een lijst van lijsten met cijfers (sudoku) en een set met de gewenste cijfers voor de evaluatie
    functie controleert of cijfers in een blok van 3x3 niet 2 keer voorkomen en of alle cijfers voorkomen
    functie moet na 'check_rij' worden aangeroepen, omdat daar de controle op aantal rijen en kolommen plaatsvindt
    output: boolean
    """
    print('Blokken 3 x 3 aan het checken...')
    # verdeel de rijen in stukken van 3
    rijen = []
    for list in check_sudoku:
        gesplitst = [list[i:i+3] for i in range(0, len(list), 3)]
        rijen.append(gesplitst[0])
        rijen.append(gesplitst[1])
        rijen.append(gesplitst[2])
    
    # Er zijn 3 rijen met 3 blokken Hieronder maak ik een set per blok aan per rij blokken
    # Vervolgens vergelijk ik deze sets met het doel. Ik doe dit voor elke rij blokken (3x)
    for i in range(3):
        square1 = set([*rijen.pop(6), *rijen.pop(3), *rijen.pop(0)])
        square2 = set([*rijen.pop(4), *rijen.pop(2), *rijen.pop(0)])
        square3 = set([*rijen.pop(2), *rijen.pop(1), *rijen.pop(0)])
        
        if (square1 != doel) or (square2 != doel) or (square3 != doel):
            print('De blokken 3 x 3 zijn onjuist ingevuld!')
            return False
    print('Blokken 3 x 3 kloppen')
    return True

# *** De familie de Jong maakt op zaterdag ook altijd de X-Sudoku. Dit zorgt voor extra constraints bij de sudoku. Dit betekent dat er ook in de twee diagonalen geen dubbele getallen voor mogen komen. De uitwerking van de puzzel van Saskia van afgelopen zaterdag vind je hier.

# help functie om de diagonalen op zaterdag te checken
def check_diagonaal(check_sudoku, doel):
    """
    input: een lijst van lijsten met cijfers (sudoku) en een set met de gewenste cijfers voor de evaluatie
    functie controleert of cijfers in de diagonalen niet 2 keer voorkomen en of alle cijfers voorkomen
    functie moet na 'check_rij' worden aangeroepen, omdat daar de controle op aantal rijen en kolommen plaatsvindt
    output: boolean
    """
    print('Diagonalen aan het checken...')
    begin = 0
    eind = 8
    diag1 = [] 
    diag2 = []
    for row in check_sudoku:
        diag1.append(row[begin])
        diag2.append(row[eind])
        begin += 1
        eind -= 1
    
    if (set(diag1) != doel) or (set(diag2) != doel):
        print('De diagonalen zijn onjuist ingevuld!')
        return False
    
    print('Diagonalen kloppen')

# controleert de sudoku
def check_sudoku(check_sudoku, doel):
    """
    input: een lijst van lijsten met cijfers (sudoku) en een set met de gewenste cijfers voor de evaluatie
    controleert of de rijen, kolommen en 3x3 kloppen
    output: boolean
    """
    dag = input('Van welke dag is de sudoku?\n').lower()
    print_sudoku(check_sudoku)

    if (dag == 'zaterdag') or (dag == 'zat'):
        if not check_diagonaal(check_sudoku, doel):
            print('De sudoku is helaas niet correct!')
            return False
    if not (check_rij(check_sudoku, doel)) or not (check_kolom(check_sudoku, doel)) or not(check_square(check_sudoku, doel)):
        print('De sudoku is helaas niet correct!')
        return False
    else:
        print('De sudoku is correct, gefeliciteerd!')
        return True

check_sudoku(sudoku, doel)
