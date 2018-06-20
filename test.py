# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import cotizador

class Test(unittest.TestCase):
	#Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.
	def test_cotizador_1(self):
		self.assertEqual("El valor calculado de su cotización es de 100.00",cotizador.cotizar_seguro('Cuenca', 25, 'hombre', 'soltero', 'infarto', 1))

	def test_cotizador_2(self):
		self.assertEqual("El valor calculado de su cotización es de 90.00",cotizador.cotizar_seguro('Machala', 40, 'hombre', 'casado', 'diabetes', 2))

	def test_cotizador_3(self):
		self.assertEqual("El valor calculado de su cotización es de 120.00",cotizador.cotizar_seguro('Quito', 18, 'mujer', 'casado', 'cancer', 3))
		
	def test_cotizador_4(self):
		self.assertEqual("El valor calculado de su cotización es de 130.00",cotizador.cotizar_seguro('Guayaquil', 25, 'mujer', 'soltero', 'osteoporosis', 4))
		
	def test_cotizador_5(self):
		self.assertEqual("El valor calculado de su cotización es de 40.00",cotizador.cotizar_seguro('Machala', 40, 'mujer', 'divorciado', 'diabetes', 0))
		
	def test_cotizador_6(self):
		self.assertEqual("El valor calculado de su cotización es de 70.00",cotizador.cotizar_seguro('Quito', 40, 'mujer', 'viudo', 'cancer', 1))
		
if __name__ == '__main__':
	unittest.main()