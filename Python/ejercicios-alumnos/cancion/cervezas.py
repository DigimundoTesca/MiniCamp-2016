'''
Botellas de cheve
'''
cuenta = 99
for i in range(0,99):
	cuenta = cuenta - 1	
	if cuenta == 1:
		print(cuenta,'botella de cerveza en la pared')
		print(cuenta,'botella de cerveza en la pared\nToma una, pasala')
	elif cuenta != 1 and cuenta != 0:
		print(cuenta,'botellas de cerveza en la pared')
		print(cuenta,'botellas de cerveza en la pared\nToma una, pasala')
	if cuenta == 0:
		print(cuenta, 'botellas de cerveza en la pared \nYa no hay chelas')
