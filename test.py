# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import cotizador

class Test(unittest.TestCase):
	#Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.
	def test_cotizador_1(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "casado", "cancer", 1),"El valor calculado de su cotización es de %.2f"%80.00)
	def test_cotizador_2(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "casado", "cancer", 2),"El valor calculado de su cotización es de %.2f"%110.00)
	def test_cotizador_3(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "casado", "cancer", 3),"El valor calculado de su cotización es de %.2f"%120.00)
	def test_cotizador_4(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "casado", "cancer", 4),"El valor calculado de su cotización es de %.2f"%140.00)
	def test_cotizador_5(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "soltero", "cancer", 0),"El valor calculado de su cotización es de %.2f"%40.00)
	def test_cotizador_6(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "viudo", "cancer", 0),"El valor calculado de su cotización es de %.2f"%40.00)
	def test_cotizador_7(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "viudo", "cancer", 1),"El valor calculado de su cotización es de %.2f"%70.00)
	def test_cotizador_8(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "viudo", "cancer", 2),"El valor calculado de su cotización es de %.2f"%100.00)
	def test_cotizador_9(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "viudo", "cancer", 3),"El valor calculado de su cotización es de %.2f"%110.00)
	def test_cotizador_10(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "viudo", "cancer", 4),"El valor calculado de su cotización es de %.2f"%130.00)
	def test_cotizador_11(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "divorciada", "cancer", 0),"El valor calculado de su cotización es de %.2f"%40.00)
	def test_cotizador_12(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "divorciada", "cancer", 1),"El valor calculado de su cotización es de %.2f"%70.00)
	def test_cotizador_13(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "divorciada", "cancer", 2),"El valor calculado de su cotización es de %.2f"%100.00)
	def test_cotizador_14(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "divorciada", "cancer", 3),"El valor calculado de su cotización es de %.2f"%110.00)
	def test_cotizador_15(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "divorciada", "cancer", 4),"El valor calculado de su cotización es de %.2f"%130.00)
	def test_cotizador_16(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 25, "masculino", "soltero", "diabetes", 0),"El valor calculado de su cotización es de %.2f"%70.00)
	def test_cotizador_17(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 25, "masculino", "casado", "diabetes", 0),"El valor calculado de su cotización es de %.2f"%30.00)
	def test_cotizador_18(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 25, "masculino", "casado", "diabetes", 1),"El valor calculado de su cotización es de %.2f"%60.00)
	def test_cotizador_19(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 25, "masculino", "casado", "diabetes", 2),"El valor calculado de su cotización es de %.2f"%90.00)
	def test_cotizador_20(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 25, "masculino", "casado", "diabetes", 3),"El valor calculado de su cotización es de %.2f"%100.00)
	def test_cotizador_21(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 25, "masculino", "casado", "diabetes", 4),"El valor calculado de su cotización es de %.2f"%120.00)
	def test_cotizador_22(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 25, "masculino", "casado", "diabetes", 8),"Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud.")
	def test_cotizador_23(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "casado", "diabetes", 8),"Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud.")
	def test_cotizador_24(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 25, "masculino", "casado", "diabetes", 10),"No se puede realizar una cotización para el valor ingresado de dependientes.")
	def test_cotizador_25(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "casado", "diabetes", 10),"No se puede realizar una cotización para el valor ingresado de dependientes.")
	def test_cotizador_26(self):
		self.assertEqual(cotizador.cotizar_seguro("Manabi", 20, "mujer", "casado", "diabetes", 10),"Saludcita no opera en la ciudad ingresada.")

if __name__ == '__main__':
	unittest.main()