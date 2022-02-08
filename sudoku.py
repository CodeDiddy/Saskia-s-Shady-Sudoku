import urllib.request, json

url = "https://community-challenge.netlify.app/data/sudoku.json"
response = urllib.request.urlopen(url)

sudoku = (json.loads(response.read()))
for list in sudoku['sudoku']:
    print(list)