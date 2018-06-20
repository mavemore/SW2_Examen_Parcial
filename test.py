# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import cotizador

class Test(unittest.TestCase):
	#Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.
	def test_cotizador_ID(self):
		self.assertEqual("","")

	def test1(self):
		res = cotizador.cotizar_seguro('Guayaquil', 20, 'mujer', 'casado', '', 2)
		self.assertEqual("El valor calculado de su cotización es de 110.00", res)
	def test2(self):
		res = cotizador.cotizar_seguro('Quito', 35, 'hombre', 'soltero', '', 0)
		self.assertEqual("El valor calculado de su cotización es de 70.00", res)
	def test1(self):
		res = cotizador.cotizar_seguro('Cuenca', 18, 'mujer', 'soltero', '', 0)
		self.assertEqual("El valor calculado de su cotización es de 40.00", res)
	def test1(self):
		res = cotizador.cotizar_seguro('Guayaquil', 25, 'hombre', 'casado', '', 1)
		self.assertEqual("El valor calculado de su cotización es de 60.00", res)
	def test1(self):
		res = cotizador.cotizar_seguro('Cuenca', 30, 'hombre', 'casado', '', 4)
		self.assertEqual("El valor calculado de su cotización es de 120.00", res)
	def test1(self):
		res = cotizador.cotizar_seguro('Machala', 35, 'mujer', 'viuda', '', 2)
		self.assertEqual("El valor calculado de su cotización es de 100.00", res)




if __name__ == '__main__':
	unittest.main()

