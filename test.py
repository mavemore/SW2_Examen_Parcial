# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import cotizador

class Test(unittest.TestCase):

	def test_cotizador_1(self):
		resultado = cotizador.cotizar_seguro('Guayaquil', 18, 'mujer', 'soltero', '', 0)
		valor = 40.00
		self.assertEqual(resultado, valor)

	def test_cotizador_2(self):
		resultado = cotizador.cotizar_seguro('Guayaquil', 38, 'mujer', 'divorciado', '', 0)
		valor = 40.00
		self.assertEqual(resultado, valor)

		
	def test_cotizador_3(self):
		resultado = cotizador.cotizar_seguro('Guayaquil', 38, 'mujer', 'divorciado', '', 1)
		valor = 70.00
		self.assertEqual(resultado, valor)
		
	def test_cotizador_4(self):
		resultado = cotizador.cotizar_seguro('Guayaquil', 38, 'mujer', 'divorciado', '', 2)
		valor = 100.00
		self.assertEqual(resultado, valor)		

	#Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.
	def test_cotizador_5(self):
		resultado = cotizador.cotizar_seguro('Guayaquil', 38, 'mujer', 'divorciado', 'osteoporosis', 3)
		valor = 110.00
		self.assertEqual(resultado, valor)
		
	def test_cotizador_6(self):
		resultado = cotizador.cotizar_seguro('Guayaquil', 38, 'mujer', 'divorciado', '', 4)
		valor = 130.00
		self.assertEqual(resultado, valor)		
		
	def test_cotizador_7(self):
		resultado = cotizador.cotizar_seguro('Guayaquil', 38, 'mujer', 'viudo', '', 0)
		valor = 40.00
		self.assertEqual(resultado, valor)
	
	def test_cotizador_8(self):
		resultado = cotizador.cotizar_seguro('Guayaquil', 38, 'mujer', 'viudo', '', 1)
		valor = 70.00
		self.assertEqual(resultado, valor)
		
	def test_cotizador_9(self):
		resultado = cotizador.cotizar_seguro('Guayaquil', 38, 'mujer', 'viudo', '', 2)
		valor = 100.00
		self.assertEqual(resultado, valor)

	def test_cotizador_10(self):
		resultado = cotizador.cotizar_seguro('Guayaquil', 38, 'mujer', 'viudo', '', 3)
		valor = 110.00
		self.assertEqual(resultado, valor)
		
	def test_cotizador_11(self):
		resultado = cotizador.cotizar_seguro('Guayaquil', 38, 'mujer', 'viudo', '', 4)
		valor = 130.00
		self.assertEqual(resultado, valor)
		
		
	def test_cotizador_12(self):
		resultado = cotizador.cotizar_seguro('Guayaquil', 25, 'mujer', 'casado', '', 1)
		valor = 80.00
		self.assertEqual(resultado, valor)
		
	def test_cotizador_13(self):
		resultado = cotizador.cotizar_seguro('Guayaquil', 25, 'mujer', 'casado', '', 2)
		valor = 110.00
		self.assertEqual(resultado, valor)

	def test_cotizador_14(self):
		resultado = cotizador.cotizar_seguro('Guayaquil', 25, 'mujer', 'casado', '', 3)
		valor = 120.00
		self.assertEqual(resultado, valor)
		
	def test_cotizador_15(self):
		resultado = cotizador.cotizar_seguro('Guayaquil', 25, 'mujer', 'casado', '', 4)
		valor = 140.00
		self.assertEqual(resultado, valor)
		
		
	def test_cotizador_16(self):
		resultado = cotizador.cotizar_seguro('Guayaquil', 18, 'hombre', 'soltero', '', 0)
		valor = 70.00
		self.assertEqual(resultado, valor)		
		

	def test_cotizador_17(self):
		resultado = cotizador.cotizar_seguro('Guayaquil', 38, 'hombre', 'viudo', '', 1)
		valor = 60.00
		self.assertEqual(resultado, valor)
		
	def test_cotizador_18(self):
		resultado = cotizador.cotizar_seguro('Guayaquil', 38, 'hombre', 'viudo', '', 2)
		valor = 90.00
		self.assertEqual(resultado, valor)
		
	def test_cotizador_19(self):
		resultado = cotizador.cotizar_seguro('Guayaquil', 38, 'hombre', 'casado', '', 3)
		valor = 100.00
		self.assertEqual(resultado, valor)
		
	def test_cotizador_20(self):
		resultado = cotizador.cotizar_seguro('Guayaquil', 38, 'hombre', 'viudo', '', 4)
		valor = 120.00
		self.assertEqual(resultado, valor)
	
		
if __name__ == '__main__':
	unittest.main()