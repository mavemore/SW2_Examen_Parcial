# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import cotizador

class Test(unittest.TestCase):
	#Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.
	def test_cotizador_ID1(self):
		dependientes = 0
		ciudad = "Guayaquil"
		edad = 25
		sexo = "mujer"
		estado_civil = "casado"
		dependientes = 1
		especial = ""
		cuota = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(cuota,"El valor calculado de su cotización es de 80.00")

	def test_cotizador_ID2(self):
		dependientes = 0
		ciudad = "Guayaquil"
		edad = 25
		sexo = "mujer"
		estado_civil = "soltero"
		dependientes = 1
		especial = ""
		cuota = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(cuota,"El valor calculado de su cotización es de 70.00")

	def test_cotizador_ID3(self):
		dependientes = 0
		ciudad = "Guayaquil"
		edad = 25
		sexo = "hombre"
		estado_civil = "soltero"
		dependientes = 1
		especial = ""
		cuota = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(cuota,"El valor calculado de su cotización es de 100.00")

if __name__ == '__main__':
	unittest.main()