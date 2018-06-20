# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import cotizador

class Test(unittest.TestCase):
	#Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.
	def test_cotizador_CP1(self):
		
		#hubo que alterar el cotizador para esta prueba
		self.assertEqual("La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años.",cotizador.cotizar_seguro("Guayaquil",17, "mujer", "soltero", "",0))
		
	def test_cotizador_CP2(self):
	
		self.assertEqual("El valor calculado de su cotización es de 80.00",cotizador.cotizar_seguro("Quito",18, "mujer", "casado", "",1))
		

	
	def test_cotizador_CP3(self):
		self.assertEqual("El valor calculado de su cotización es de 70.00",cotizador.cotizar_seguro("Quito",20, "hombre", "soltero", "",0))
	
	
	def test_cotizador_CP4(self):
		self.assertEqual("El valor calculado de su cotización es de 70.00",cotizador.cotizar_seguro("Cuenca",25, "mujer", "divorciada", "",1))
	
	
	def test_cotizador_CP5(self):
		self.assertEqual("El valor calculado de su cotización es de 100.00",cotizador.cotizar_seguro("Quito",35, "hombre", "casado", "",3))
	
	
	def test_cotizador_CP6(self):
		self.assertEqual("El valor calculado de su cotización es de 70.00",cotizador.cotizar_seguro("Cuenca",40, "hombre", "soltero", "",0))
	
	
	def test_cotizador_CP7(self):
		self.assertEqual("El valor calculado de su cotización es de 110.00",cotizador.cotizar_seguro("Guayaquil",40, "mujer", "casado", "osteoporosis",2))
	
	
	def test_cotizador_CP7(self):
		self.assertEqual("Saludcita no opera en la ciudad ingresada.",cotizador.cotizar_seguro("Ambato",32, "mujer", "soltero", "",0))
		
		
if __name__ == '__main__':
	unittest.main()