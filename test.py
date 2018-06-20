# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from cotizador import *

class Test(unittest.TestCase):
	#Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.
	def test_cotizador_1(self):
		ciudad = 178
		edad = 18
		sexo = "Hombre"
		estado_civil = "soltero"
		dependientes = 0
		especial = "osteoporosis"
		result = cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual("Saludcita no opera en la ciudad ingresada.",result)

	def test_cotizador_2(self):
		ciudad = "Guayaquil"
		edad = -1
		sexo = "Hombre"
		estado_civil = "soltero"
		dependientes = 0
		especial = "osteoporosis"
		result = cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual("La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años.",result)

	def test_cotizador_3(self):
		ciudad = "Guayaquil"
		edad = 17
		sexo = "Hombre"
		estado_civil = "soltero"
		dependientes = 0
		especial = "osteoporosis"
		result = cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual("La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años.",result)

	def test_cotizador_4(self):
		ciudad = "Guayaquil"
		edad = 76
		sexo = "Hombre"
		estado_civil = "soltero"
		dependientes = 0
		especial = "osteoporosis"
		result = cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual("La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años.",result)

	def test_cotizador_4(self):
		ciudad = "Guayaquil"
		edad = 19
		sexo = "Hombre"
		estado_civil = "soltero"
		dependientes = 0
		especial = "diabetes"
		result = cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual("El valor calculado de su cotización es de 70.00",result)

	def test_cotizador_5(self):
		ciudad = "Guayaquil"
		edad = 19
		sexo = "mujer"
		estado_civil = "soltero"
		dependientes = 0
		especial = "diabetes"
		result = cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual("El valor calculado de su cotización es de 40.00",result)

	def test_cotizador_6(self):
		ciudad = "Guayaquil"
		edad = 19
		sexo = "mujer"
		estado_civil = "casado"
		dependientes = 1
		especial = "diabetes"
		result = cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual("El valor calculado de su cotización es de 80.00",result)

	def test_cotizador_9(self):
		ciudad = "Guayaquil"
		edad = 19
		sexo = "mujer"
		estado_civil = "casado"
		dependientes = 4
		especial = "diabetes"
		result = cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual("El valor calculado de su cotización es de 140.00",result)

	def test_cotizador_11(self):
		ciudad = "Guayaquil"
		edad = 19
		sexo = "hombre"
		estado_civil = "casado"
		dependientes = 4
		especial = "diabetes"
		result = cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual("El valor calculado de su cotización es de 120.00",result)

	def test_cotizador_12(self):
		ciudad = "Guayaquil"
		edad = 19
		sexo = "hombre"
		estado_civil = "casado"
		dependientes = 1
		especial = "diabetes"
		result = cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual("El valor calculado de su cotización es de 60.00",result)

	def test_cotizador_13(self):
		ciudad = "Guayaquil"
		edad = 19
		sexo = "hombre"
		estado_civil = "casado"
		dependientes = 11
		especial = "diabetes"
		result = cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual("No se puede realizar una cotización para el valor ingresado de dependientes.",result)

if __name__ == '__main__':
	unittest.main()