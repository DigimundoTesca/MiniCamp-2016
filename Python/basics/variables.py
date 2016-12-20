entero = 40

flotante = 4.2

print( entero, flotante)

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
mi_lista.append(2)
mi_lista.insert(0, 'nueva cadena')
mi_lista.remove(22)
print(mi_lista)