# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import cotizador

class Test(unittest.TestCase):
	#Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.
	def test_cotizador_cp1(self):
		edad = 20
		ciudad = 'Guayaquil'
		sexo = 'hombre'
		estado_civil = 'soltero'
		especial = 'osteoporosis'
		dependientes = 0
		cotizacion = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(cotizacion , 'El valor calculado de su cotización es de 70.00')

	def test_cotizador_cp2(self):
		edad = 20
		ciudad = 'Quito'
		sexo = 'mujer'
		estado_civil = 'casado'
		especial = 'infarto'
		dependientes = 1
		cotizacion = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(cotizacion , 'El valor calculado de su cotización es de 80.00')

	def test_cotizador_cp3(self):
		edad = 20
		ciudad = 'Cuenca'
		sexo = 'mujer'
		estado_civil = 'divorciado'
		especial = 'diabetes'
		dependientes = 2
		cotizacion = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(cotizacion , 'El valor calculado de su cotización es de 100.00')

	def test_cotizador_cp4(self):
		edad = 20
		ciudad = 'Machala'
		sexo = 'mujer'
		estado_civil = 'divorciado'
		especial = 'cancer'
		dependientes = 3
		cotizacion = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(cotizacion , 'El valor calculado de su cotización es de 110.00')

	def test_cotizador_cp5(self):
		edad = 20
		ciudad = 'Cuenca'
		sexo = 'mujer'
		estado_civil = 'divorciado'
		especial = 'cancer'
		dependientes = 4
		cotizacion = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(cotizacion , 'El valor calculado de su cotización es de 130.00')
	

	def test_cotizador_cp6(self):
		edad = 20
		ciudad = 'Cuenca'
		sexo = 'XYZ'
		estado_civil = 'divorciado'
		especial = 'cancer'
		dependientes = 4
		cotizacion = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(cotizacion , '')

	def test_cotizador_cp7(self):
		edad = 20
		ciudad = 'Cuenca'
		sexo = 'mujer'
		estado_civil = 'ABC'
		especial = 'cancer'
		dependientes = 4
		cotizacion = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(cotizacion , '')

if __name__ == '__main__':
	unittest.main()