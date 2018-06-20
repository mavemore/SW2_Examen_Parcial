# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import cotizador

class Test(unittest.TestCase):
	#Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.

	###############################################################
	#MUJER CASADA##################################################
	###############################################################
	def test_cotizador_C01(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "casado", "no", 1)
		esperado = "El valor calculado de su cotización es de 80.00"
		self.assertEqual(esperado,calculado)

	def test_cotizador_C02(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "casado", "no", 2)
		esperado = "El valor calculado de su cotización es de 110.00"
		self.assertEqual(esperado,calculado)

	def test_cotizador_C03(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "casado", "no", 3)
		esperado = "El valor calculado de su cotización es de 120.00"
		self.assertEqual(esperado,calculado)

	def test_cotizador_C04(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "casado", "no", 4)
		esperado = "El valor calculado de su cotización es de 140.00"
		self.assertEqual(esperado,calculado)

	def test_cotizador_C05(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "casado", "no", 5)
		esperado = "Solo se puede realizar la cotización para hasta 4 dependientes en línea. Por favor acérquese a la agencia y presente una solicitud."
		self.assertEqual(esperado,calculado)

	###############################################################
	#MUJER NO CASADA###############################################
	###############################################################

	def test_cotizador_C06(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "soltero", "no", 0)
		esperado = "El valor calculado de su cotización es de 40.00"
		self.assertEqual(esperado,calculado)

	def test_cotizador_C07(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "soltero", "no", 1)
		esperado = "El valor calculado de su cotización es de 70.00"
		self.assertEqual(esperado,calculado)

	def test_cotizador_C08(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "soltero", "no", 2)
		esperado = "El valor calculado de su cotización es de 100.00"
		self.assertEqual(esperado,calculado)

	def test_cotizador_C09(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "soltero", "no", 3)
		esperado = "El valor calculado de su cotización es de 110.00"
		self.assertEqual(esperado,calculado)

	def test_cotizador_C10(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "soltero", "no", 4)
		esperado = "El valor calculado de su cotización es de 130.00"
		self.assertEqual(esperado,calculado)

	def test_cotizador_C11(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "soltero", "no", 5)
		esperado = "Solo se puede realizar la cotización para hasta 4 dependientes en línea. Por favor acérquese a la agencia y presente una solicitud."
		self.assertEqual(esperado,calculado)

	###############################################################
	#HOMBRE SOLTERO################################################
	###############################################################

	def test_cotizador_C12(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "hombre", "soltero", "no", 0)
		esperado = "El valor calculado de su cotización es de 70.00"
		self.assertEqual(esperado,calculado)

	def test_cotizador_C13(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "hombre", "soltero", "no", 1)
		esperado = "El valor calculado de su cotización es de 100.00"
		self.assertEqual(esperado,calculado)

	def test_cotizador_C14(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "hombre", "soltero", "no", 2)
		esperado = "El valor calculado de su cotización es de 130.00"
		self.assertEqual(esperado,calculado)

	def test_cotizador_C15(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "hombre", "soltero", "no", 3)
		esperado = "El valor calculado de su cotización es de 140.00"
		self.assertEqual(esperado,calculado)

	def test_cotizador_C16(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "hombre", "soltero", "no", 4)
		esperado = "El valor calculado de su cotización es de 160.00"
		self.assertEqual(esperado,calculado)

	def test_cotizador_C17(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "hombre", "soltero", "no", 5)
		esperado = "Solo se puede realizar la cotización para hasta 4 dependientes en línea. Por favor acérquese a la agencia y presente una solicitud."
		self.assertEqual(esperado,calculado)

	###############################################################
	#HOMBRE NO SOLTERO#############################################
	###############################################################

	def test_cotizador_C18(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "hombre", "viudo", "no", 0)
		esperado = "El valor calculado de su cotización es de 30.00"
		self.assertEqual(esperado,calculado)

	def test_cotizador_C19(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "hombre", "viudo", "no", 1)
		esperado = "El valor calculado de su cotización es de 60.00"
		self.assertEqual(esperado,calculado)

	def test_cotizador_C20(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "hombre", "viudo", "no", 2)
		esperado = "El valor calculado de su cotización es de 90.00"
		self.assertEqual(esperado,calculado)

	def test_cotizador_C21(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "hombre", "viudo", "no", 3)
		esperado = "El valor calculado de su cotización es de 100.00"
		self.assertEqual(esperado,calculado)

	def test_cotizador_C22(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "hombre", "viudo", "no", 4)
		esperado = "El valor calculado de su cotización es de 120.00"
		self.assertEqual(esperado,calculado)

	def test_cotizador_C23(self):
		calculado = cotizador.cotizar_seguro("Guayaquil", 20, "hombre", "viudo", "no", 5)
		esperado = "Solo se puede realizar la cotización para hasta 4 dependientes en línea. Por favor acérquese a la agencia y presente una solicitud."
		self.assertEqual(esperado,calculado)


if __name__ == '__main__':
	unittest.main()