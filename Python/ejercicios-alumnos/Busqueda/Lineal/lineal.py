'''
Programa que realizará la tarea del método find
'''
lista = ['1','2','3']
c = input('Ingresa lo que quieres buscar\t')
def busqueda(lista):
	for i in lista:
		if i == c:
			print('True')
		elif i != c:
			print('False')
			break

#Intento de hacer recursiva la busqueda
# opc = input('¿Nueva busqueda?(y/n)')
# while opc == 'y':
	busqueda(lista)
