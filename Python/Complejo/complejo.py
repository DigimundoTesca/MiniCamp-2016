import math

class Complejo(object):
	"""docstring for Complejo"""
	def __init__(self, real, imaginario):
		super(Complejo, self).__init__()
		self.real = real
		self.img = imaginario

	def abs(self):
		print math.sqrt( (self.real * self.real) + (self.img * self.img) )


def main():
	numero = Complejo(3,4)
	print 'parte real:', numero.real
	print numero.img
	numero.abs()


if __name__ == '__main__':
	main()
