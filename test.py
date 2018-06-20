# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import cotizador

class Test(unittest.TestCase):
	#Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.
	def test_cotizador_CP0(self):
		valor_total = cotizador.calcular_cuota_basica(0) + cotizador.calcular_valores_adicionales(20, 'mujer', 'soltero', 'ninguna')		
		self.assertEqual(valor_total, 40.0)

	def test_cotizador_CP1(self):
		valor_total = cotizador.calcular_cuota_basica(0) + cotizador.calcular_valores_adicionales(20, 'mujer', 'casado', 'ninguna')		
		self.assertEqual(valor_total, 50.0)

	def test_cotizador_CP2(self):
		valor_total = cotizador.calcular_cuota_basica(1) + cotizador.calcular_valores_adicionales(20, 'mujer', 'soltero', 'ninguna')		
		self.assertEqual(valor_total, 70.0)

	def test_cotizador_CP3(self):
		valor_total = cotizador.calcular_cuota_basica(1) + cotizador.calcular_valores_adicionales(20, 'mujer', 'casado', 'ninguna')		
		self.assertEqual(valor_total, 80.0)

	def test_cotizador_CP4(self):
		valor_total = cotizador.calcular_cuota_basica(2) + cotizador.calcular_valores_adicionales(20, 'mujer', 'soltero', 'ninguna')		
		self.assertEqual(valor_total, 100.0)

	def test_cotizador_CP5(self):
		valor_total = cotizador.calcular_cuota_basica(2) + cotizador.calcular_valores_adicionales(20, 'mujer', 'casado', 'ninguna')		
		self.assertEqual(valor_total, 110.0)

	def test_cotizador_CP6(self):
		valor_total = cotizador.calcular_cuota_basica(3) + cotizador.calcular_valores_adicionales(20, 'mujer', 'soltero', 'ninguna')		
		self.assertEqual(valor_total, 110.0)

	def test_cotizador_CP7(self):
		valor_total = cotizador.calcular_cuota_basica(3) + cotizador.calcular_valores_adicionales(20, 'mujer', 'casado', 'ninguna')		
		self.assertEqual(valor_total, 120.0)

	def test_cotizador_CP8(self):
		valor_total = cotizador.calcular_cuota_basica(4) + cotizador.calcular_valores_adicionales(20, 'mujer', 'soltero', 'ninguna')		
		self.assertEqual(valor_total, 130.0)

	def test_cotizador_CP9(self):
		valor_total = cotizador.calcular_cuota_basica(4) + cotizador.calcular_valores_adicionales(20, 'mujer', 'casado', 'ninguna')		
		self.assertEqual(valor_total, 140.0)

	def test_cotizador_CP10(self):
		valor_total = cotizador.calcular_cuota_basica(0) + cotizador.calcular_valores_adicionales(20, 'hombre', 'soltero', 'ninguna')		
		self.assertEqual(valor_total, 70.0)

	def test_cotizador_CP11(self):
		valor_total = cotizador.calcular_cuota_basica(0) + cotizador.calcular_valores_adicionales(20, 'hombre', 'casado', 'ninguna')		
		self.assertEqual(valor_total, 30.0)

	def test_cotizador_CP12(self):
		valor_total = cotizador.calcular_cuota_basica(1) + cotizador.calcular_valores_adicionales(20, 'hombre', 'soltero', 'ninguna')		
		self.assertEqual(valor_total, 100.0)

	def test_cotizador_CP13(self):
		valor_total = cotizador.calcular_cuota_basica(1) + cotizador.calcular_valores_adicionales(20, 'hombre', 'casado', 'ninguna')		
		self.assertEqual(valor_total, 60.0)

	def test_cotizador_CP14(self):
		valor_total = cotizador.calcular_cuota_basica(2) + cotizador.calcular_valores_adicionales(20, 'hombre', 'soltero', 'ninguna')		
		self.assertEqual(valor_total, 130.0)

	def test_cotizador_CP15(self):
		valor_total = cotizador.calcular_cuota_basica(2) + cotizador.calcular_valores_adicionales(20, 'hombre', 'casado', 'ninguna')		
		self.assertEqual(valor_total, 90.0)

	def test_cotizador_CP16(self):
		valor_total = cotizador.calcular_cuota_basica(3) + cotizador.calcular_valores_adicionales(20, 'hombre', 'soltero', 'ninguna')		
		self.assertEqual(valor_total, 140.0)

	def test_cotizador_CP17(self):
		valor_total = cotizador.calcular_cuota_basica(3) + cotizador.calcular_valores_adicionales(20, 'hombre', 'casado', 'ninguna')		
		self.assertEqual(valor_total, 100.0)

	def test_cotizador_CP18(self):
		valor_total = cotizador.calcular_cuota_basica(4) + cotizador.calcular_valores_adicionales(20, 'hombre', 'soltero', 'ninguna')		
		self.assertEqual(valor_total, 160.0)

	def test_cotizador_CP19(self):
		valor_total = cotizador.calcular_cuota_basica(4) + cotizador.calcular_valores_adicionales(20, 'hombre', 'casado', 'ninguna')		
		self.assertEqual(valor_total, 120.0)

if __name__ == '__main__':
	unittest.main()