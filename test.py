# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import cotizador

class Test(unittest.TestCase):
	#Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.
	def test_cotizador_1(self):
		edad = 18
		genero = 'mujer'
		estado_civil = 'soltero'
		ciudad = 'Quito'
		especial = 'ninguna'
		dependiente = 0

		total = cotizador.cotizar_seguro(ciudad,edad,genero,estado_civil,especial,dependiente)
		self.assertEqual(total,"El valor calculado de su cotización es de 40.00")

	def test_cotizador_2(self):
			edad = 35
			genero = 'hombre'
			estado_civil = 'soltero'
			ciudad = 'Quito'
			especial = 'ninguna'
			dependiente = 0
			total = cotizador.cotizar_seguro(ciudad,edad,genero,estado_civil,especial,dependiente)
			self.assertEqual(total,"El valor calculado de su cotización es de 70.00")

	def test_cotizador_3(self):
			edad = 35
			genero = 'mujer'
			estado_civil = 'casado'
			ciudad = 'Guayaquil'
			especial = 'ninguna'
			dependiente = 1

			total = cotizador.cotizar_seguro(ciudad,edad,genero,estado_civil,especial,dependiente)
			self.assertEqual(total,"El valor calculado de su cotización es de 80.00")

	def test_cotizador_4(self):
			edad = 25
			genero = 'mujer'
			estado_civil = 'casado'
			ciudad = 'Guayaquil'
			especial = 'ninguna'
			dependiente = 2

			total = cotizador.cotizar_seguro(ciudad,edad,genero,estado_civil,especial,dependiente)
			self.assertEqual(total,"El valor calculado de su cotización es de 110.00")
if __name__ == '__main__':
	unittest.main()