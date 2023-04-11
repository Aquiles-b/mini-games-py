import pyautogui as pg
import time
import os

grid = []

while True:
	linha = list(input(f"Linha {len(grid) + 1}:"))
	convertido = []

	for num in linha:
		convertido.append(int(num))

	grid.append(convertido)

	if len(grid) == 9:
		break

	print("Linha" + str(len(grid)) + " Feita")

os.system("cls")

time.sleep(2)

print()

def bonito(su):
	for l in range(0,9):
		for c in range(0,9): 
			print(su[l][c], end=" ")
			if c==2:
				print("|", end=" ")
			elif c==5:
				print("|", end=" ")
		print()
		if l ==2:
			print("-"*22)	
		elif l ==5:
			print("-"*22)
	print()	
		
def possivel(x,y,num):

	for i in range(0,9):
		if grid[y][i] == num and i != x:
			return False

	for i in range(0,9):
		if grid[i][x] == num and i != y:
			return False

	h = (x // 3) * 3
	v = (y // 3) * 3

	for l in range(h,h+3):
		for c in range(v, v+3):
			if grid[c][l] == num:
				return False

	return True

def escrever(bo):
	final = []

	for lista in bo:
		for num in lista:
			final.append(str(num))

	contador = []

	for num in final:
		pg.press(num)
		pg.hotkey('right')
		contador.append(num)
		if len(contador)%9 == 0:
			pg.hotkey('down')
			for i in range(8):
				pg.hotkey('left')

def resolve():
	for l in range(0,9):
		for c in range(0,9):
			if grid[l][c] == 0:
				for num in range(1,10):
					if possivel(c,l,num):
						grid[l][c] = num
						resolve()
						grid[l][c] = 0
				return
	bonito(grid)
	escrever(grid)
			
resolve()

