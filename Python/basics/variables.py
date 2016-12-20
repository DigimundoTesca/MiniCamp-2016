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
nombre = input('Ingresa tu nombre: ')
edad = input('Ingresa tu edad: ')
mensaje_1 = 'Hola ' + nombre + ', tu edad es de ' + edad + ' años.'
mensaje_2 = 'Hola %s, tu edad es de %s años.' % (nombre, edad)
mensaje_3 = 'Hola {}, tu edad es de {} años.'.format(nombre, edad)
print(mensaje_1)
print(mensaje_2)
print(mensaje_3)

