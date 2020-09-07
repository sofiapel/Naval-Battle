#!/usr/bin/env python3



def leerArchivo():
	tupla_barcos = []
	tupla_x = []
	tupla_y = []
	count= 0
	f = open('Salida.txt', 'r')
	barcos = f.readlines()
	print(barcos)
	for barco in barcos:
		# ~ barco = list(string)
		# ~ print(barco)
		for i in range(0, len(barco)-1):
			if barco[i] in ['A','B','C','D','E','F','G','H','I','J']:
				# ~ print(barco[i])
				tupla_x.append(barco[i])
			if barco[i] in ['1','2','3','4','5','6','7','8','9']:
				if barco[int(i)] == '0':
					break
				elif barco[int(i)+ 1] == '0':
					# ~ print('10')
					tupla_y.append(10)
				else:
					# ~ print(barco[i])
					tupla_y.append(int(barco[i]))

	# [(A,10),(B,10),(C,10),(D,10)]
    #      ^
	print("NUEVA LINEA")
	print(tupla_x)
	print(tupla_y)


	for i in range (0,len(tupla_x)):
		s = (tupla_x[i],tupla_y[i])
		# ~ print(s)
		tupla_barcos.append(s)
	return tupla_barcos
				
				
def tableroCorrecto(tupla):
	tableroVacio = [[ 'v' for i in range(10) ] for j in range(10) ] #cambiarle el nombre a la variable
	letritas = {'A': 0, 'B': 1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}
	solucion = tupla
	first_tuple_elements = []
	second_tuple_elements = []
	
	for tupla in solucion:
		first_tuple_elements.append(tupla[0])
		second_tuple_elements.append(tupla[1])
		
	# ~ for i in range(0, len(second_tuple_elements)):
		# ~ print(first_tuple_elements[i])
		# ~ print(second_tuple_elements[i])
		
	# ~ print(letritas[first_tuple_elements[0]])
		
	for i in range (0,len(first_tuple_elements)):
		tableroVacio[letritas[first_tuple_elements[i]]][int(second_tuple_elements[i])-1] = 'b' #first tuple elements es una letra aaaaa
	
	# ~ for i in range(0,len(tableroVacio)):
		# ~ print(tableroVacio[i])
	return tableroVacio
		
# ~ tableroCorrecto(leerArchivo())

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
	
def ganadorPartida(tupla, tablero):
	# ~ tablero = tableroCorrecto(tupla)
	solucion = tableroCorrecto(tupla)
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
