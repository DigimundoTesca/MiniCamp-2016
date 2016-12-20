class Perro(object):
	def __init__(self):
		self.patas = 4
		self.ojos = 1.5
		self.orejas = 2
		self.cola = 0.5
		self.dientes = 3
		self.hambre = 0
		self.locura = 0

	def get_patas(self):
		return self.patas

	def set_nivel_hambre(self, nivel_hambre):
		nivel_hambre = int(nivel_hambre)
		if nivel_hambre >= 10:
			self.locura = nivel_hambre * 2
		else:
			self.locura = 0
	
	def get_locura(self):
		return self.locura


perro_loco = Perro()

nivel_locura = input('Ingresa el nivel de hambre del perro')

perro_loco.set_nivel_hambre(nivel_locura)

print('Nivel de locura:', perro_loco.get_locura())