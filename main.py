from sudoku import *

# zet de locatie van de sudoku in een variabele
url = 'https://community-challenge.netlify.app/data/sudoku.json'

# Maak een Sudoku-object voor de te controleren sudoku
sudoku = Sudoku(url)

# Check de sudoku
sudoku.check_sudoku()

# Check de zaterdag sudoku 
url_zat = 'https://community-challenge.netlify.app/data/sudoku.json'
sudoku_zaterdag = Sudoku(url_zat)
sudoku_zaterdag.check_sudoku()
