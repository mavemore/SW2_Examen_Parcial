# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from cotizador import *

class Test(unittest.TestCase):
	#Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.
	def test_cotizador_ID(self):
		self.assertEqual("","")
	
	def test_CP1(self):
		"""
		Calcula el valor total para los datos del CP1 ("Cuenca", 23, "mujer", "soltera", "", 0) y verifica su validez
		"""	
		self.assertEqual("El valor calculado de su cotización es de %.2f"%(40),cotizar_seguro("Cuenca", 23, "mujer", "soltera", "", 0))

	def test_CP2(self):
		"""
		Calcula el valor total para los datos del CP2 ("Cuenca", 23, "mujer", "casado", "", 1) y verifica su validez
		"""	
		self.assertEqual("El valor calculado de su cotización es de %.2f"%(80),cotizar_seguro("Cuenca", 23, "mujer", "casado", "", 1))
	
	def test_CP3(self):
		"""
		Calcula el valor total para los datos del CP3 ("Cuenca", 23, "mujer", "casado", "", 2) y verifica su validez
		"""	
		self.assertEqual("El valor calculado de su cotización es de %.2f"%(110),cotizar_seguro("Cuenca", 23, "mujer", "casado", "", 2))
	
	def test_CP4(self):
		"""
		Calcula el valor total para los datos del CP4 ("Cuenca", 23, "mujer", "casado", "", 3) y verifica su validez
		"""	
		self.assertEqual("El valor calculado de su cotización es de %.2f"%(120),cotizar_seguro("Cuenca", 23, "mujer", "casado", "", 3))
	
	def test_CP5(self):
		"""
		Calcula el valor total para los datos del CP5 ("Cuenca", 23, "mujer", "soltera", "", 4) y verifica su validez
		"""	
		self.assertEqual("El valor calculado de su cotización es de %.2f"%(130),cotizar_seguro("Cuenca", 23, "mujer", "soltera", "", 4))
		
	def test_CP6(self):
		"""
		Calcula el valor total para los datos del CP6 ("Quito", 28, "hombre", "casado", "", 2) y verifica su validez
		"""	
		self.assertEqual("El valor calculado de su cotización es de %.2f"%(90),cotizar_seguro("Quito", 28, "hombre", "casado", "", 2))
		
	def test_CP7(self):
		"""
		Calcula el valor total para los datos del CP7 ("Quito", 28, "hombre", "soltero", "", 1) y verifica su validez
		"""	
		self.assertEqual("El valor calculado de su cotización es de %.2f"%(100),cotizar_seguro("Quito", 28, "hombre", "soltero", "", 1))
	
	def test_CP8(self):
		"""
		Calcula el valor total para los datos del CP8 ("Quito", 28, "hombre", "soltero", "", 2) y verifica su validez
		"""	
		self.assertEqual("El valor calculado de su cotización es de %.2f"%(130),cotizar_seguro("Quito", 28, "hombre", "soltero", "", 2))
	
	def test_CP9(self):
		"""
		Calcula el valor total para los datos del CP9 ("Quito", 28, "hombre", "soltero", "", 3) y verifica su validez
		"""	
		self.assertEqual("El valor calculado de su cotización es de %.2f"%(140),cotizar_seguro("Quito", 28, "hombre", "soltero", "", 3))
	
	def test_CP10(self):
		"""
		Calcula el valor total para los datos del CP8 ("Quito", 28, "hombre", "soltero", "", 4) y verifica su validez
		"""	
		self.assertEqual("El valor calculado de su cotización es de %.2f"%(160),cotizar_seguro("Quito", 28, "hombre", "soltero", "", 4))
	
if __name__ == '__main__':
	unittest.main()