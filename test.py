# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import cotizador

class Test(unittest.TestCase):
	#Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.
	def test_cotizador_1(self):
	    valor_cotizado = cotizador.cotizar_seguro('Guayaquil', 20, 'mujer', 'soltero', '', 0)
	    self.assertEqual(valor_cotizado, "El valor calculado de su cotización es de 40.00")

	def test_cotizador_2(self):
	    valor_cotizado = cotizador.cotizar_seguro('Quito', 30, 'mujer', 'casado', '', 1)
	    self.assertEqual(valor_cotizado, "El valor calculado de su cotización es de 80.00")

	def test_cotizador_3(self):
	    valor_cotizado = cotizador.cotizar_seguro('Cuenca', 35, 'mujer', 'casado', '', 2)
	    self.assertEqual(valor_cotizado, "El valor calculado de su cotización es de 110.00")

	def test_cotizador_4(self):
	    valor_cotizado = cotizador.cotizar_seguro('Machala', 40, 'mujer', 'casado', '', 3)
	    self.assertEqual(valor_cotizado, "El valor calculado de su cotización es de 120.00")

	def test_cotizador_5(self):
	    valor_cotizado = cotizador.cotizar_seguro('Guayaquil', 33, 'mujer', 'casado', '', 4)
	    self.assertEqual(valor_cotizado, "El valor calculado de su cotización es de 140.00")

	def test_cotizador_6(self):
	    valor_cotizado = cotizador.cotizar_seguro('Quito', 25, 'hombre', 'soltero', '', 0)
	    self.assertEqual(valor_cotizado, "El valor calculado de su cotización es de 70.00")

	def test_cotizador_7(self):
	    valor_cotizado = cotizador.cotizar_seguro('Cuenca', 39, 'mujer', 'viudo', '', 0)
	    self.assertEqual(valor_cotizado, "El valor calculado de su cotización es de 40.00")

	def test_cotizador_8(self):
	    valor_cotizado = cotizador.cotizar_seguro('Machala', 29, 'mujer', 'divorciado', '', 0)
	    self.assertEqual(valor_cotizado, "El valor calculado de su cotización es de 40.00")

	def test_cotizador_9(self):
	    valor_cotizado = cotizador.cotizar_seguro('Quito', 36, 'mujer', 'divorciado', '', 1)
	    self.assertEqual(valor_cotizado, "El valor calculado de su cotización es de 70.00")

	def test_cotizador_10(self):
	    valor_cotizado = cotizador.cotizar_seguro('Cuenca', 25, 'mujer', 'divorciado', '', 2)
	    self.assertEqual(valor_cotizado, "El valor calculado de su cotización es de 100.00")

if __name__ == '__main__':
	unittest.main()