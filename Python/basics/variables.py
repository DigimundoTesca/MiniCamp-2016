'''
Ejemplo de operaciones sencillas
'''
x = 19
y = 4

# Suma
result = x + y
print('Suma', result)

# Resta
result = x - y
print('Resta', result)

# Multipicación
result = x * y
print('Multiplicación', result)

# División
result = x / y
print('División', result)

# División (enteros)
result = x // y
print('Disivión entera', result)

# Potencia
result = x ** y
print('Potencia', result)


'''
Strings
'''
nombre = 'El chido'
edad = '43'
# nombre = input('Ingresa tu nombre: ')
# edad = input('Ingresa tu edad: ')
mensaje_1 = 'Hola ' + nombre + ', tu edad es de ' + edad + ' años.'
mensaje_2 = 'Hola %s, tu edad es de %s años.' % (nombre, edad)
mensaje_3 = 'Hola {}, tu edad es de {} años.'.format(nombre, edad)
print(mensaje_1)
print(mensaje_2)
print(mensaje_3)

# Strings como listas
print(mensaje_1[0])
print(mensaje_1[8])
print(mensaje_1[0:10])
print(mensaje_1[0:20:2])
print(mensaje_1[-1])

# Formato
s1 = 'primer texto'
s2 = 'segundo texto'
result = '{a} {b}'.format(a=s1, b=s2)
print(result)

# Búsqueda
cadena = 'Este es un texto random'
pos = cadena.find('un')
print(pos)
nueva_cadena = result.replace('e', 'E')
print(nueva_cadena)



"""
Listas
"""
mi_lista = ['hola', 23, 23.12, True, 'Otro texto', False]

# Modificar un elemento
mi_lista[3] = True
print(mi_lista)

# Conocer tamaño de la lista
print( len(mi_lista))

# Añadir un elemento al final de la lista
mi_lista.append(2)
print(mi_lista)

# Insertar un elemento en una posición de la lsita
mi_lista.insert(0, 'nueva cadena')
print(mi_lista)

# Eliminar un elemento de nuestra lista
mi_lista.remove(23)
print(mi_lista)

# Saber si existe un elemento en nuestra lista
print (23 in mi_lista)
print ('hola' in mi_lista)

# Concatenacion de listas
L1 = [1, 2, 3, 'hola', True]
L2 = ['ey!', 3, -12.3, False]
print(L1 + L2)

# Cocatenar n veces una lista
L3 = ['ja', 'ja', 'ja']
print(L3 * 5)

# Porcion de una secuencia (no inclusiva)
print('\n\nMi lista:', mi_lista)
print( mi_lista[1:2])

# Porcion de una secuencia (no inclusiva) con saltos
print(mi_lista[1:6:1])
print(mi_lista[1:6:2])

# Busqueda
ent_list = [4, 12, 121, -4 , -90, 0]

# Elemento más pequeño en la lista
print('Mínimo: ', min(ent_list))

# Elemento más grande en la lista
print('Máximo: ', max(ent_list))


'''
Tuplas
'''

mi_tupla = (23, -1212, True, (1, False, 'ja'))
print(mi_tupla)
print(mi_tupla[2])

# Las tuplas son inmutables
# No esta perimitdo :
# mi_tupla[1] = 'Hola'

# Longitud
len(mi_tupla)

# Empaquetado y desempaquetado
a = 12
b = -12.2
c = 'Texto'
e = a, b, c
print(e)

x, y, z = e
print(x, y, z)


'''
Diccionarios 
'''
diccionario = {'x':1, 'y':10, 'z':-10}
print(diccionario)

dic_dias = {}
dic_dias['Lunes'] = 100
dic_dias['Martes'] = 1212
dic_dias['Miercoles'] = [-100]
dic_dias['Jueves'] = ['Hola', True]
dic_dias['Viernes'] = []
print(dic_dias)

print(dic_dias['Jueves'])
print(dic_dias['Jueves'][0])

# Controlando errores de petición de valores
# print(dic_dias['Domingo'])
print(dic_dias.get('Domingo'))

# Recorrer un diccionario
for dia in dic_dias:
	print(dia, ':', dic_dias[dia])

# Impresion de valores condicionados
for dia, codigos in dic_dias.items():
	print(dia, ':', codigos)

print(dic_dias.items())

d = {'x':20, 'y':5}
if 'x' in d:
	print(d['x'])

if 'z' in d:
	print(d['z'])

if 'y' in d:
	print(d['y'])


'''
Manejo de Excepciones 
'''
# Esto marca un error
# print(10/0)

try:
	result = 10 / 0
except:
	print('No se permite la división entre 0')