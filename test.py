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

	def test_calcular_cuota_basica1(self):
		cuota = cotizador.calcular_cuota_basica(0)
		self.assertEqual(cuota,30)

	def test_calcular_cuota_basica2(self):
		cuota = cotizador.calcular_cuota_basica(1)
		self.assertEqual(cuota,60)

	def test_calcular_cuota_basica3(self):
		cuota = cotizador.calcular_cuota_basica(2)
		self.assertEqual(cuota,90)

	def test_calcular_cuota_basica3(self):
		cuota = cotizador.calcular_cuota_basica(3)
		self.assertEqual(cuota,100)

	def test_calcular_cuota_basica3(self):
		cuota = cotizador.calcular_cuota_basica(4)
		self.assertEqual(cuota,120)

	def test_calcular_valores_adicionales1(self):
		calcular = cotizador.calcular_valores_adicionales(18, "hombre", "casado", "")
		self.assertEqual(calcular,0)

	def test_calcular_valores_adicionales2(self):
		calcular = cotizador.calcular_valores_adicionales(18, "mujer", "soltero", "")
		self.assertEqual(calcular,10)

	def test_calcular_valores_adicionales3(self):
		calcular = cotizador.calcular_valores_adicionales(40, "mujer", "soltero", "osteoporosis")
		self.assertEqual(calcular,10)

	def test_calcular_valores_adicionales4(self):
		calcular = cotizador.calcular_valores_adicionales(41, "hombre", "soltero", "infarto")
		self.assertEqual(calcular,50)

	def test_calcular_valores_adicionales5(self):
		calcular = cotizador.calcular_valores_adicionales(61, "hombre", "soltero", "cancer")
		self.assertEqual(calcular,50)

	def test_calcular_valores_adicionales6(self):
		calcular = cotizador.calcular_valores_adicionales(61, "mujer", "soltero", "cancer")
		self.assertEqual(calcular,60)

if __name__ == '__main__':
	unittest.main()