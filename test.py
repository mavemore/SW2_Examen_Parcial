# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from cotizador import * 

class Test(unittest.TestCase):
	#Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.
	def test_cotizador_CP1(self):
		self.assertEqual(cotizar_seguro("Guayaquil",20,"mujer","soltero","",0),"El valor calculado de su cotización es de 40.00")
	def test_cotizador_CP2(self):
		self.assertEqual(cotizar_seguro("Guayaquil",20,"hombre","soltero","",0),"El valor calculado de su cotización es de 70.00")
	def test_cotizador_CP3(self):
		self.assertEqual(cotizar_seguro("Guayaquil",20,"mujer","casado","",1),"El valor calculado de su cotización es de 80.00")
	def test_cotizador_CP4(self):
		self.assertEqual(cotizar_seguro("Guayaquil",20,"mujer","divorciada","",0),"El valor calculado de su cotización es de 40.00")
	def test_cotizador_CP5(self):
		self.assertEqual(cotizar_seguro("Guayaquil",20,"mujer","viuda","",0),"El valor calculado de su cotización es de 40.00")
	def test_cotizador_CP6(self):
		self.assertEqual(cotizar_seguro("Guayaquil",20,"mujer","casado","",2),"El valor calculado de su cotización es de 110.00")
	def test_cotizador_CP7(self):
		self.assertEqual(cotizar_seguro("Guayaquil",20,"mujer","casado","",3),"El valor calculado de su cotización es de 120.00")
	def test_cotizador_CP8(self):
		self.assertEqual(cotizar_seguro("Guayaquil",20,"mujer","casado","",4),"El valor calculado de su cotización es de 140.00")
	def test_cotizador_CP9(self):
		self.assertEqual(cotizar_seguro("Guayaquil",20,"hombre","soltero","",1),"El valor calculado de su cotización es de 100.00")
	def test_cotizador_CP10(self):
		self.assertEqual(cotizar_seguro("Guayaquil",20,"hombre","soltero","",2),"El valor calculado de su cotización es de 130.00")
	def test_cotizador_CP11(self):
		self.assertEqual(cotizar_seguro("Guayaquil",20,"hombre","soltero","",3),"El valor calculado de su cotización es de 140.00")
	def test_cotizador_CP12(self):
		self.assertEqual(cotizar_seguro("Guayaquil",20,"hombre","soltero","",4),"El valor calculado de su cotización es de 160.00")
	def test_cotizador_CP13(self):
		self.assertEqual(cotizar_seguro("Guayaquil",20,"hombre","casado","",2),"El valor calculado de su cotización es de 90.00")
	def test_cotizador_CP14(self):
		self.assertEqual(cotizar_seguro("Guayaquil",20,"hombre","casado","",3),"El valor calculado de su cotización es de 100.00")
	def test_cotizador_CP15(self):
		self.assertEqual(cotizar_seguro("Guayaquil",20,"hombre","casado","",4),"El valor calculado de su cotización es de 120.00")
if __name__ == '__main__':
	unittest.main()