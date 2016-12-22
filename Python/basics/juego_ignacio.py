import time
from time import sleep
import random

op = ('piedra','papel','tijera','lagarto','spock')
separador= '-' * 50
a = 0

while True:
	op_p1 = input('Elige: piedra, papel, tijeras, lagarto o spock\n')
	
	if op_p1 not in op:
		print('opcion invalida, como tu prro :v')
		continue
	
	print('pensando...')
	sleep(0.5)
	
	op_pc=random.choice(op)
	print(('la pc eligió {}\n').format(op_pc))
	
	sleep(0.5)


	if op_p1=="tijeras" and op_pc=="papel":
		a = 1
	elif op_p1=="papel" and op_pc=="piedra":
		a = 1
	elif op_p1=="piedra" and op_pc=="lagarto":
		a = 1
	elif op_p1=="lagarto" and op_pc=="spock":
		a = 1
	elif op_p1=="spock" and op_pc=="tijeras":
		a = 1
	elif op_p1=="tijeras" and op_pc=="lagarto":
		a = 1
	elif op_p1=="lagarto" and op_pc=="papel":
		a = 1
	elif op_p1=="papel" and op_pc=="spock":
		a = 1
	elif op_p1=="spock" and op_pc=="piedra":
		a = 1
	elif op_p1=="piedra" and op_pc=="tijeras":
		a = 1

	if op_pc == op_p1:
		print('empataste compy, intentalo otra vez\n')
	elif a == 1:
		print('anuma, ganaztez!\n')
	elif a==0:
		print('perdistee :v\n')

print('yolo\n')