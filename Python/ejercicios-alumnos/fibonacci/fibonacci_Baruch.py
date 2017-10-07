'''
Secuencia Fibonacci
'''
n = int(input('Ingrese el valor maximo\t'))
def Fibonacci(n):
	i = 1 
	c = 0
	while i <= n:
		c = c + i
		i += 1
	print(c)

Fibonacci(n)