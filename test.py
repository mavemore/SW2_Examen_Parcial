# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import cotizador

class Test(unittest.TestCase):
	#Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.
	def test_cotizador_ID(self):
		self.assertEqual("","")

	def test_cotizador_1(self):
		luis = Cliente("Guayaquil", 18, 'hombre', 'soltero', 'ninguno', 0)

		cotizacion_de_luis = cotizador.cotizar_seguro(luis.ciudad, luis.edad, 
									luis.sexo, luis.estado_civil,
									 luis.especial, luis.dependientes)
		esperado = "El valor calculado de su cotización es de %.2f" % 70
		self.assertEqual(cotizacion_de_luis, esperado)



	def test_cotizador_2(self):
		monica = Cliente("Quito", 25, 'mujer', 'divorciada', 'ninguno', 0)

		cotizacion_de_monica = cotizador.cotizar_seguro(monica.ciudad, monica.edad, 
									monica.sexo, monica.estado_civil,
									 monica.especial, monica.dependientes)
		esperado = "El valor calculado de su cotización es de %.2f" % 40
		self.assertEqual(cotizacion_de_monica, esperado)


	def test_cotizador_3(self):
		juanita = Cliente("Cuenca", 20, 'mujer', 'casado', 'ninguno', 1)

		cotizacion_de_juanita = cotizador.cotizar_seguro(juanita.ciudad, juanita.edad, 
									juanita.sexo, juanita.estado_civil,
									 juanita.especial, juanita.dependientes)
		esperado = "El valor calculado de su cotización es de %.2f" % 80
		self.assertEqual(cotizacion_de_juanita, esperado)
	

	def test_cotizador_4(self):
		johan = Cliente("Machala", 30, 'hombre', 'divorciado', 'ninguno', 1)

		cotizacion_de_johan = cotizador.cotizar_seguro(johan.ciudad, johan.edad, 
									johan.sexo, johan.estado_civil,
									 johan.especial, johan.dependientes)
		esperado = "El valor calculado de su cotización es de %.2f" % 60
		self.assertEqual(cotizacion_de_johan, esperado)
	

	def test_cotizador_5(self):
		luis = Cliente("Guayaquil", 20, 'hombre', 'casado', 'ninguno', 4)

		cotizacion_de_luis = cotizador.cotizar_seguro(luis.ciudad, luis.edad, 
									luis.sexo, luis.estado_civil,
									 luis.especial, luis.dependientes)
		esperado = "El valor calculado de su cotización es de %.2f" % 120
		self.assertEqual(cotizacion_de_luis, esperado)
	

	def test_cotizador_6(self):
		luis = Cliente("Guayaquil", 20, 'hombre', 'casado', 'ninguno', 4)

		cotizacion_de_luis = cotizador.cotizar_seguro(luis.ciudad, luis.edad, 
									luis.sexo, luis.estado_civil,
									 luis.especial, luis.dependientes)
		esperado = "El valor calculado de su cotización es de %.2f" % 120
		self.assertEqual(cotizacion_de_luis, esperado)
	
	def test_cotizador_7(self):
		luis = Cliente("Quito", 40, 'hombre', 'soltero', 'ninguno', 4)

		cotizacion_de_luis = cotizador.cotizar_seguro(luis.ciudad, luis.edad, 
									luis.sexo, luis.estado_civil,
									 luis.especial, luis.dependientes)
		esperado = "El valor calculado de su cotización es de %.2f" % 160
		self.assertEqual(cotizacion_de_luis, esperado)
	

	def test_cotizador_8(self):
		luis = Cliente("Quito", 20, 'mujer', 'divorciado', 'ninguno', 5)

		cotizacion_de_luis = cotizador.cotizar_seguro(luis.ciudad, luis.edad, 
									luis.sexo, luis.estado_civil,
									 luis.especial, luis.dependientes)
		esperado = "Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud."
		self.assertEqual(cotizacion_de_luis, esperado)
	

	def test_cotizador_9(self):
		luis = Cliente("Loja", 20, 'mujer', 'casado', 'ninguno', 1)

		cotizacion_de_luis = cotizador.cotizar_seguro(luis.ciudad, luis.edad, 
									luis.sexo, luis.estado_civil,
									 luis.especial, luis.dependientes)
		esperado = "Saludcita no opera en la ciudad ingresada."
		self.assertEqual(cotizacion_de_luis, esperado)

	def test_cotizador_10(self):
		luis = Cliente("Machala", 20, 'mujer', 'casado', 'ninguno', 12)

		cotizacion_de_luis = cotizador.cotizar_seguro(luis.ciudad, luis.edad, 
									luis.sexo, luis.estado_civil,
									 luis.especial, luis.dependientes)
		esperado =  "No se puede realizar una cotización para el valor ingresado de dependientes."
		self.assertEqual(cotizacion_de_luis, esperado)
	

class Cliente():

	def __init__(self, ciudad, edad, sexo, estado_civil, especial, dependientes):
		self.ciudad = ciudad
		self.edad = edad
		self.sexo = sexo
		self.estado_civil = estado_civil
		self.especial = especial
		self.dependientes = dependientes


if __name__ == '__main__':
	unittest.main()