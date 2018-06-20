# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import cotizador

class Test(unittest.TestCase):
	#Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.

	def test_cotizador_1(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'mujer', 'soltero', ' ', 10) 
		self.assertEqual('No se puede realizar una cotización para el valor ingresado de dependientes.', valor)

	def test_cotizador_2(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'mujer', 'soltero', ' ', 7) 
		self.assertEqual('Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud.', valor)
#	----------						Mujer NO casada						----------
	def test_cotizador_3(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'mujer', 'soltero', ' ', 0) 
		self.assertEqual('El valor calculado de su cotización es de 40.00', valor)

	def test_cotizador_4(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'mujer', 'soltero', ' ', 1) 
		self.assertEqual('El valor calculado de su cotización es de 70.00', valor)

	def test_cotizador_5(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'mujer', 'soltero', ' ', 2) 
		self.assertEqual('El valor calculado de su cotización es de 100.00', valor)

	def test_cotizador_6(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'mujer', 'soltero', ' ', 3) 
		self.assertEqual('El valor calculado de su cotización es de 110.00', valor)

	def test_cotizador_7(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'mujer', 'soltero', ' ', 4) 
		self.assertEqual('El valor calculado de su cotización es de 130.00', valor)
#	----------						Mujer Casada						----------
	def test_cotizador_8(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'mujer', 'casado', ' ', 0) 
		self.assertEqual('El valor calculado de su cotización es de 50.00', valor)

	def test_cotizador_9(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'mujer', 'casado', ' ', 1) 
		self.assertEqual('El valor calculado de su cotización es de 80.00', valor)

	def test_cotizador_10(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'mujer', 'casado', ' ', 2) 
		self.assertEqual('El valor calculado de su cotización es de 110.00', valor)

	def test_cotizador_11(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'mujer', 'casado', ' ', 3) 
		self.assertEqual('El valor calculado de su cotización es de 120.00', valor)

	def test_cotizador_12(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'mujer', 'casado', ' ', 4) 
		self.assertEqual('El valor calculado de su cotización es de 140.00', valor)
#	----------						Hombre No soltero					----------
	def test_cotizador_13(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'hombre', 'casado', ' ', 0) 
		self.assertEqual('El valor calculado de su cotización es de 30.00', valor)

	def test_cotizador_14(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'hombre', 'casado', ' ', 1) 
		self.assertEqual('El valor calculado de su cotización es de 60.00', valor)

	def test_cotizador_15(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'hombre', 'casado', ' ', 2) 
		self.assertEqual('El valor calculado de su cotización es de 90.00', valor)

	def test_cotizador_16(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'hombre', 'casado', ' ', 3) 
		self.assertEqual('El valor calculado de su cotización es de 100.00', valor)

	def test_cotizador_17(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'hombre', 'casado', ' ', 4) 
		self.assertEqual('El valor calculado de su cotización es de 120.00', valor)
#	----------						Hombre soltero					----------
	def test_cotizador_18(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'hombre', 'soltero', ' ', 0) 
		self.assertEqual('El valor calculado de su cotización es de 70.00', valor)

	def test_cotizador_19(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'hombre', 'soltero', ' ', 1) 
		self.assertEqual('El valor calculado de su cotización es de 100.00', valor)

	def test_cotizador_20(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'hombre', 'soltero', ' ', 2) 
		self.assertEqual('El valor calculado de su cotización es de 130.00', valor)

	def test_cotizador_21(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'hombre', 'soltero', ' ', 3) 
		self.assertEqual('El valor calculado de su cotización es de 140.00', valor)

	def test_cotizador_22(self):
		valor = cotizador.cotizar_seguro('Guayaquil', 40, 'hombre', 'soltero', ' ', 4) 
		self.assertEqual('El valor calculado de su cotización es de 160.00', valor)



if __name__ == '__main__':
	unittest.main()