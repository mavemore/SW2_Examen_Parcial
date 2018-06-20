# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import cotizador

class Test(unittest.TestCase):
	#Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.
	#cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
	def test_cotizador_1(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil",20,"mujer","casado","",1),"El valor calculado de su cotización es de 80.00")
	def test_cotizador_2(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil",20,"mujer","divorciada","",0),"El valor calculado de su cotización es de 40.00")
	def test_cotizador_3(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil",20,"mujer","soltero","",0),"El valor calculado de su cotización es de 40.00")
	def test_cotizador_4(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "viuda", "", 0),"El valor calculado de su cotización es de 40.00")
	def test_cotizador_5(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 20, "hombre", "soltero", "", 0),"El valor calculado de su cotización es de 70.00")
	def test_cotizador_6(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 45, "mujer", "casado", "", 1),"El valor calculado de su cotización es de 60.00")
	def test_cotizador_7(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 45, "mujer", "soltera", "", 0),"El valor calculado de su cotización es de 30.00")
	def test_cotizador_8(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 45, "mujer", "casada", "", 3),"El valor calculado de su cotización es de 100.00")
	def test_cotizador_9(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 45, "mujer", "casada", "", 4),"El valor calculado de su cotización es de 120.00")
	def test_cotizador_10(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 45, "mujer", "casada", "osteoporosis", 3),"El valor calculado de su cotización es de 135.00")
	def test_cotizador_11(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 45, "hombre", "soltero", "infarto", 0),"El valor calculado de su cotización es de 80.00")
	def test_cotizador_12(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 45, "hombre", "casado", "infarto", 3),"El valor calculado de su cotización es de 150.00")
if __name__ == '__main__':
	unittest.main()