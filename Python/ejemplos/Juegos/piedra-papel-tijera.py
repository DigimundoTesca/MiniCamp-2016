#!/usr/bin/env python
# -*-coding:utf-8-*-

import time
from time import sleep
import random

rayas = '-' * 35
opciones = ('piedra', 'papel', 'tijera')

while True:
    x = input('Elije uno: piedra, papel, tijera: ')
    if x not in opciones:
        print ('No hagas trampa!!!')
        continue

    pc = random.choice(opciones)
    sleep(0.5)

    print (("Computadora eligió {}.").format(pc))

    if x == pc:
        sleep(0.5)
        print (("\nEmpate.\n{}").format(rayas))
    elif x == "piedra" and pc == "tijera":
        sleep(0.5)
        print (("\nGanaste.piedra gana tijera\n{}").format(rayas))
    elif x == "papel" and pc == "piedra":
        sleep(0.5)
        print (("\nGanaste.papel gana roca\n{}").format(rayas))
    elif x == "tijera" and pc == "papel":
        sleep(0.5)
        print (("\nGanaste.tijera gana papel\n{}").format(rayas))
    else:
        sleep(0.5)
        print (("\nPerdiste. {} gana {}\n{}").format(pc,x,rayas))
input()