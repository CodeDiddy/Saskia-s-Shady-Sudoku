import urllib.request, json

# lees de sudoku in een variabele
url = "https://community-challenge.netlify.app/data/sudoku.json"
response = urllib.request.urlopen(url)

sudoku_json = (json.loads(response.read()))

# sla de rijen (lists) uit de sudoku op in een variabele voor de werkbaarheid
sudoku = sudoku_json['sudoku']

# Controleer of alle rijen kloppen, horizontaal en verticaal. De input vind je in sudoku.json.

# elke rij, kolom, 3x3 en diagonaal mag maar 1 keer een getal vanaf 1 t/m 9 staan. Hiervoor gebruik ik een set 
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
        return False
    for list in check_sudoku:
        if (set(list) != doel):
            print('List is niet gelijk aan doel')
            print(set(list), " != ", doel)
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
            return False
    print('Kolommen kloppen')
    return True


# TODO: controle functie voor de 3x3 maken en aan deze functie toevoegen
def check_sudoku(check_sudoku, doel):
    """
    input: een lijst van lijsten met cijfers (sudoku) en een set met de gewenste cijfers voor de evaluatie
    controleert of de rijen, kolommen en 3x3 kloppen
    output: boolean
    """
    if not (check_rij(check_sudoku, doel)) or not (check_kolom(check_sudoku, doel)):
        print('FOUT')
        return False
    else:
        print('De sudoku is correct')
        return True

check_sudoku(sudoku, doel)