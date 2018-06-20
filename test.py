# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import cotizador

class Test(unittest.TestCase):
	#Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.
	def test_cotizador_ID(self):
		# MUJER 20 AÑOS CASADA CON VARIACION DE DEPENDIENCIA (0..4)
		# P1
		self.assertEqual(cotizador.calcular_cuota_basica(1) +
						 cotizador.calcular_valores_adicionales(20, "mujer","casado","")
						 , 80)
		# P11
		self.assertEqual(cotizador.calcular_cuota_basica(0) +
						 cotizador.calcular_valores_adicionales(20, "mujer", "casado", "")
						 , 50)
		# P12
		self.assertEqual(cotizador.calcular_cuota_basica(2) +
						 cotizador.calcular_valores_adicionales(20, "mujer", "casado", "")
						 , 110)
		# P13
		self.assertEqual(cotizador.calcular_cuota_basica(3) +
						 cotizador.calcular_valores_adicionales(20, "mujer", "casado", "")
						 , 120)
		# P14
		self.assertEqual(cotizador.calcular_cuota_basica(4) +
						 cotizador.calcular_valores_adicionales(20, "mujer", "casado", "")
						 , 140)

		# HOMBRE 20 AÑOS SOLTERO
		# P2
		self.assertEqual(cotizador.calcular_cuota_basica(0) +
						 cotizador.calcular_valores_adicionales(20, "hombre", "soltero", "")
						 , 70)

		#MUJER 21 años soltera con Variacion de dependencia
		# P3
		self.assertEqual(cotizador.calcular_cuota_basica(2) +
						 cotizador.calcular_valores_adicionales(21, "mujer", "soltero", "")
						 , 100)
		# P31
		self.assertEqual(cotizador.calcular_cuota_basica(0) +
						 cotizador.calcular_valores_adicionales(21, "mujer", "soltero", "")
						 , 40)
		# P32
		self.assertEqual(cotizador.calcular_cuota_basica(1) +
						 cotizador.calcular_valores_adicionales(21, "mujer", "soltero", "")
						 , 70)
		# P33
		self.assertEqual(cotizador.calcular_cuota_basica(3) +
						 cotizador.calcular_valores_adicionales(21, "mujer", "soltero", "")
						 , 110)

		# P4
		self.assertEqual(cotizador.calcular_cuota_basica(3) +
						 cotizador.calcular_valores_adicionales(39, "mujer", "viuda", "")
						 , 110)
		# P5
		self.assertEqual(cotizador.calcular_cuota_basica(4) +
						 cotizador.calcular_valores_adicionales(39, "mujer", "divorciada", "")
						 , 130)



if __name__ == '__main__':
	unittest.main()