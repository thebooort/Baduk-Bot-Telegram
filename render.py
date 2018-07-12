import re
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def grid_to_coords(grid):
    grid_size = (40,40)
    coords = [grid[i] * grid_size[i] for i in range(2)] * 2
    coords[2] += grid_size[0]
    coords[3] += grid_size[1]
    return coords

#Draw the board
grid_size = (40,40)
grid_size_1 = 40
# board = Image.new('RGB', [10*x for x in grid_size], (255,204,153))

# Open wood board image and crops it to the desired size 
image_source = Image.open("images/wood_board.jpg")
area = (0, 0, grid_size_1*10, grid_size_1*10) # (initial x, initial y, width, height)
board = image_source.crop(area)



for i in range(1,10):
    i = i * 40
    for j in range(1,10):
        j = j * 40
        ImageDraw.Draw(board).line([i,j,i,40] , width=1)
        ImageDraw.Draw(board).line([i,j,40,j] , width=1)


lista_de_letras =  ['A','B','C','D','E','F','G','H','J']
lista_de_numeros = ['1','2','3','4','5','6','7','8','9']

for i in range(0,9):
    letra = lista_de_letras[i]
    ImageDraw.Draw(board).text((20,1.14*(i+1)*34),letra,fill=(0,0,0))

for i in range(0,9):
    numero = lista_de_numeros[i]
    ImageDraw.Draw(board).text((1.14*(i+1)*35,20),numero,fill=(0,0,0))

board.show()
