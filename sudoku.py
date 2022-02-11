import urllib.request, json

class Sudoku:
    
    doel = {1, 2, 3, 4, 5, 6, 7, 8, 9} 

    def __init__(self, url):
        self.url = url
        self.sudoku = self.haal_sudoku()

    def haal_sudoku(self):
        response = urllib.request.urlopen(self.url)
        sudoku_json = (json.loads(response.read()))
        return sudoku_json['sudoku']
    
    # print de ingevulde sudoku
    def print_sudoku(self):
        print('')
        print('*' * 10, end='')
        print(' SUDOKU ', end='')
        print('*' * 11)
        for row in self.sudoku:
            print('*', end='')
            print(row, end='')
            print('*')
        print('*' * 29)
        print('')
    
    # help functie om de rijen te checken
    def _check_rij(self, doel):
        """
        input: een lijst van lijsten met cijfers (sudoku) en een set met de gewenste cijfers voor de evaluatie
        functie controleert of er genoeg rijen in de sudoku zitten
        functie controleert of cijfers in een rij niet 2 keer voorkomen en of alle cijfers voorkomen
        output: boolean
        """
        print('Rijen aan het checken...')
        if len(self.sudoku) != 9:
            print(f"Sudoku heeft {len(self.sudoku)} rijen.")
            print('De sudoku is niet volledig ingevuld!')
            print('')
            return False
        for list in self.sudoku:
            if (set(list) != doel):
                print(set(list), " != ", doel)
                print('De rijen zijn onjuist ingevuld!')
                print('')
                return False
        print('Rijen kloppen')
        return True


    # help functie om de kolommen te checken
    def _check_kolom(self, doel):
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
                kolom.append(self.sudoku[j][i])
            if set(kolom) != doel:
                print('De kolommen zijn onjuist ingevuld!')
                print('')
                return False
        print('Kolommen kloppen')
        return True

    # ** Controleer nu ook of de "hokjes" van 3x3 kloppen.

    # help functie om de blokken (3x3) te checken
    def _check_square(self, doel):
        """
        input: een lijst van lijsten met cijfers (sudoku) en een set met de gewenste cijfers voor de evaluatie
        functie controleert of cijfers in een blok van 3x3 niet 2 keer voorkomen en of alle cijfers voorkomen
        functie moet na 'check_rij' worden aangeroepen, omdat daar de controle op aantal rijen en kolommen plaatsvindt
        output: boolean
        """
        print('Blokken 3 x 3 aan het checken...')
        # verdeel de rijen in stukken van 3
        rijen = []
        for list in self.sudoku:
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
                print('')
                return False
        print('Blokken 3 x 3 kloppen')
        return True

    # help functie om de diagonalen op zaterdag te checken
    def _check_diagonaal(self, doel):
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
        for row in self.sudoku:
            diag1.append(row[begin])
            diag2.append(row[eind])
            begin += 1
            eind -= 1
        
        if (set(diag1) != doel) or (set(diag2) != doel):
            print('De diagonalen zijn onjuist ingevuld!')
            print('')
            return False
        
        print('Diagonalen kloppen')

    # controleert de sudoku
    def check_sudoku(self):
        """
        input: een lijst van lijsten met cijfers (sudoku) en een set met de gewenste cijfers voor de evaluatie
        controleert of de rijen, kolommen en 3x3 kloppen
        output: boolean
        """
        dag = input('Van welke dag is de sudoku?\n').lower()
        self.print_sudoku()

        if (dag == 'zaterdag') or (dag == 'zat'):
            if not self._check_diagonaal(self.doel):
                print('De sudoku is helaas niet correct!')
                print('')
                return False
        if not (self._check_rij(self.doel)) or not (self._check_kolom(self.doel)) or not(self._check_square(self.doel)):
            print('De sudoku is helaas niet correct!')
            print('')
            return False
        else:
            print('De sudoku is correct, gefeliciteerd!')
            print('')
            return True