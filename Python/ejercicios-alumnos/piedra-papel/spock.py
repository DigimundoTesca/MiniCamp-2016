'''
Piedra papel y tijeras avanzado
'''
#!/usr/bin/env python
# -*-coding:utf-8-*-

import time
from time import sleep
import random

separador =  '-' * 50
opc = ('piedra', 'papel', 'tijeras', 'lagarto', 'spock')

while True:
	usr = input('Elige uno: piedra, papel, tijeras, lagarto, spock\t')
	if usr not in opc:
		print('Escoge bien shabo >:v')
		continue
	pc = random.choice(opc)
	sleep(0.5)


	print(("La PC escogió {}").format(pc))

	if usr == pc:
		sleep(0.5)
		print('\tAh numa, empataron goe :v\t\n{}'.format(separador))

	elif usr == "piedra" and pc == "papel":
		sleep(0.3)
		print("\tPerdiste mijo :'v\t\n{}".format(separador))
		sleep(0.3)
	elif  usr == "papel" and pc == "piedra":
		print("\tGanaste PogChamp\t\n{}".format(separador))
		sleep(0.3)
	elif usr == "tijeras" and pc == "papel":
		print("\t Ganaste PogChamp\t\n{}".format(separador))
		sleep(0.3)
	elif usr == "papel" and pc == "tijeras":
		print("\tPerdiste :'v\t\n{}".format(separador))
		sleep(0.3)
	elif usr == "lagarto" and pc == "spock":
		print("\tGanaste PogChamp v:\t\n{}".format(separador))
		sleep(0.3)
	elif usr == "spock" and pc == "lagarto":
		print("\tPerdiste v:\t\n{}".format(separador))
		sleep(0.3)
	elif  usr == "spock" and pc == "piedra":
		print("\tGanaste TwT\t\n{}".format(separador))
		sleep(0.3)
	elif usr == "piedra" and pc == "spock":
		print("\tPerdiste\t\n{}".format(separador))
		sleep(0.3)
	elif usr == "tijeras" and pc == "lagarto":
		print("\tGanaste :3\t\n{}".format(separador))
		sleep(0.3)
	elif usr == "lagarto" and pc == "tijeras":
		print("\tPerdiste :'v' v:\t\n{}".format(separador))
		sleep(0.3)
	elif usr == "papel" and pc == "spock":
		print("\tGanaste PogChamp v:\t\n{}".format(separador))
		sleep(0.3)
	elif usr == "spock" and pc == "papel":
		print("\tPerdiste :'v v:\t\n{}".format(separador))
		sleep(0.3)
	elif usr == "lagarto" and pc == "papel":
		print("\tGanaste PogChamp v:\t\n{}".format(separador))
		sleep(0.3)
	elif usr == "papel" and pc == "lagarto":
		print("\tPierdes v:\t\n{}".format(separador))
		sleep(0.3)
	elif usr == "lagarto" and pc == "piedra":
		print("\tPierdes v:\t\n{}".format(separador))
		sleep(0.3)
	elif usr == "piedra" and pc == "lagarto":
		print("\tGanaste PogChamp v:\t\n{}".format(separador))
		sleep(0.3)
	elif usr == "tijeras" and pc == "spock":
		print("\tPerdiste PogChamp v:\t\n{}".format(separador))
		sleep(0.3)
	elif usr == "spock" and pc == "tijeras":
		print("\tGanaste PogChamp v:\t\n{}".format(separador))
		sleep(0.3)
	elif usr == "piedra" and pc == "tijeras":
		print("\tGanaste PogChamp v:\t\n{}".format(separador))
		sleep(0.3)
	elif usr == "tijeras" and pc == "piedra":
		print("\tPerdiste PogChamp v:\t\n{}".format(separador))
		sleep(0.3)