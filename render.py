import re
from PIL import Image, ImageDraw, ImageFont, ImageFilter

class Render():

    #Inicialiaze the Render class with an empty board
	#Tablero can have 3 values, 0,1,2. 0 for 9x9, 1 for 12x12 and 2 for 18x18
	def __init__(self, turn=True,tablero=0):
		self.turn = turn
		self.grid_size = (40,40)
		if(tablero==0):
			self.board = self.create_board_9()
		elif(tablero==1):
			self.board = self.create_board_13()
		else:
			self.board = self.create_board_19()
		#self.piece_locations =

    #Create an empty 9x9 Go board
	def create_board_9(self):

        #board = Image.new('RGB', [10*x for x in self.grid_size], (255,204,153))
		image_source = Image.open("images/wood_board.jpg")
		area = (0, 0, grid_size_1*10, grid_size_1*10) # (initial x, initial y, width, height)
		board = image_source.crop(area)
		format = 40
		for i in range(1,10):
			i = i * format
			for j in range(1,10):
				j = j * format
				ImageDraw.Draw(board).line([i,j,i,40] , width=1,fill=(0,0,0))
				ImageDraw.Draw(board).line([i,j,40,j] , width=1,fill=(0,0,0))


		lista_de_letras =  ['A','B','C','D','E','F','G','H','J']
		lista_de_numeros = ['1','2','3','4','5','6','7','8','9']

		for i in range(0,9):
			letra = lista_de_letras[i]
			ImageDraw.Draw(board).text((20,1.14*(i+1)*34),letra,fill=(0,0,0))

		for i in range(0,9):
			numero = lista_de_numeros[i]
			ImageDraw.Draw(board).text((1.14*(i+1)*35,20),numero,fill=(0,0,0))

		return board

	#Create an empty 13x13 Go board
	def create_board_13(self):

		board_size = 14 #Always one more than the real board size
		image_source = Image.open("images/wood_board.jpg")
		area = (0, 0, self.grid_size[0]*board_size, self.grid_size[0]*board_size) # (initial x, initial y, width, height)
		board = image_source.crop(area)

		for i in range(1,board_size):
		    i = i * self.grid_size[0]
		    for j in range(1,board_size):
		        j = j * self.grid_size[0]
		        ImageDraw.Draw(board).line([i,j,i,self.grid_size[0]] , width=1,fill=(0,0,0))
		        ImageDraw.Draw(board).line([i,j,self.grid_size[0],j] , width=1,fill=(0,0,0))

		lista_de_letras =  ['A','B','C','D','E','F','G','H','J','K','L','M','O']
		lista_de_numeros = ['1','2','3','4','5','6','7','8','9','10','11','12','13']

		for i in range(0,board_size-1):
		    letra = lista_de_letras[i]
		    ImageDraw.Draw(board).text((20,1.15*(i+1)*34),letra,fill=(0,0,0))

		for i in range(0,board_size-1):
		    numero = lista_de_numeros[i]
		    ImageDraw.Draw(board).text((1.14*(i+1)*35,20),numero,fill=(0,0,0))

		return board

	#Create an empty 19x19 Go board
	def create_board_19(self):
		#board = Image.new('RGB', [10*x for x in self.grid_size], (255,204,153))
		image_source = Image.open("images/wood_board.jpg")
		board_size = 20
		area = (0, 0, self.grid_size[0]*board_size, self.grid_size[0]*board_size) # (initial x, initial y, width, height)
		board = image_source.crop(area)
		format = 40
		for i in range(1,board_size):
			i = i * format
			for j in range(1,board_size):
				j = j * format
				ImageDraw.Draw(board).line([i,j,i,format] , width=1,fill=(0,0,0))
				ImageDraw.Draw(board).line([i,j,format,j] , width=1,fill=(0,0,0))


		lista_de_letras =  ['A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T']
		lista_de_numeros = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
		list_size = board_size-1
		for i in range(0,list_size):
			letra = lista_de_letras[i]
			ImageDraw.Draw(board).text((20,1.14*(i+1)*34),letra,fill=(0,0,0))

		for i in range(0,list_size):
			numero = lista_de_numeros[i]
			ImageDraw.Draw(board).text((1.14*(i+1)*35,20),numero,fill=(0,0,0))

		return board

	def show_board(self):
		self.board.show()






Tablero = Render(tablero=1)

Tablero.show_board()