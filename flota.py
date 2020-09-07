#!/usr/bin/env python3



def leerArchivo():
	tuplas_barcos = []
	tupla_x = []
	tupla_y = []
	count= 0
	f = open('Salida.txt', 'r')
	barcos = f.readlines()
	for barco in barcos:
		for i in range(0, len(barco)-1):
			if barco[i] in ['A','B','C','D','E','F','G','H','I','J']:
				tupla_x.append(barco[i])
			if barco[i] in ['1','2','3','4','5','6','7','8','9']:
				if barco[int(i)+ 1] == '0':
					tupla_y.append(10)
				else:
					tupla_y.append(int(barco[i]))

	for i in range(len(tupla_x)):
		s = (tupla_x[i],tupla_y[i])
		tuplas_barcos.append(s)
	return tuplas_barcos


def tableroCorrecto(tuplas):
	solucion = [[ 'v' for i in range(10) ] for j in range(10) ]
	letritas = {'A': 0, 'B': 1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}

	for tupla in tuplas:
		solucion[letritas[tupla[0]]][tupla[1]-1] = 'b'

	return solucion

def Tocau(tupla,tablero,fila,columna):
	coordenadas = tupla
	lista = tableroCorrecto(coordenadas)
	letritas = {'A': 0, 'B': 1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}
	# ~ columna = input()
	# ~ fila = int(input())
	columnaa = letritas[columna]
	filaa = fila - 1
	if lista[columnaa][filaa] == 'b':
		# ~ print('re tocado')
		tablero[columnaa][filaa] = 'T'
	else:
		# ~ print('agua')
		tablero[columnaa][filaa] = 'A'
	return tablero
		
# ~ Tocau(leerArchivo()) 
	
def ganadorPartida(tuplas, tablero):
	# ~ tablero = tableroCorrecto(tupla)
	solucion = tableroCorrecto(tuplas)
	count = 0
	hundidos = 0
	for item in solucion:
		hundidos += item.count('b')
		
	for i in range(10):
		for j in range(10):
			if tablero[i][j] == 'T':      #tendria q ser h aca o t si no consigo como hundir el barco 
				 count += 1
		
	# ~ print(hundidos)
		

	if (count == hundidos):
		# ~ print("TRUE")
		return True
	else:
		# ~ print("FALSE")
		return False
		
# ~ ganadorPartida(leerArchivo())

def mostrarAlgo(tablero):
	# ~ tablero = [ [ 'v' for i in range(10) ] for j in range(10) ]
	letras = ['A','B','C','D','E', 'F', 'G', 'H', 'I', 'J']

	for i in range(10):
		if (i == 0):
			print("1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10|")
		for j in range(10):
			print(f'{tablero[i][j]} |', end = ' ')	
		print(f'{letras[i]}')

# ~ mostrarAlgo()
def JuegaNaval():
	tablero = [ [ 'v' for i in range(10) ] for j in range(10) ]
	mostrarAlgo(tablero)
	
	while(ganadorPartida(leerArchivo(), tablero) != True): #Falta esto
		print("Ingrese una letra o la palabra salir para abandonar el juego")
		columna = input()
		if (columna == "salir"):
			break
		else:
			print("Ingrese un numero")
			fila = int(input())
			tablero = Tocau(leerArchivo(),tablero,fila,columna)
			mostrarAlgo(tablero)
		
			#muestratablero1
			#ingresaposicion
			#leeposicion
			#muestra tablero1 con la posicion elegida	
	if(ganadorPartida(leerArchivo(),tablero) == True):
		print("Ganaste muy bien 10")


JuegaNaval()
