# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import cotizador

class Test(unittest.TestCase):
	#Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.
	def test_cotizador_CP1(self):
		ciudad = 'Guayaquil'
		edad = 25
		sexo = 'mujer'
		estado_civil = 'casado'
		especial = None
		dependientes = 1
		cuota = cotizador.calcular_cuota_basica(dependientes)
		adicional = cotizador.calcular_valores_adicionales(
			edad,
			sexo,
			estado_civil,
			especial
		)
		cotizacion = cotizador.cotizar_seguro(
			ciudad,
			edad,
			sexo,
			estado_civil,
			especial,
			dependientes
		)
		resultado_esperado = "El valor calculado de su cotización es de 80.00"
		self.assertEqual(cotizacion, resultado_esperado)

	def test_cotizador_CP2(self):
		ciudad = 'Guayaquil'
		edad = 25
		sexo = 'mujer'
		estado_civil = 'casado'
		especial = None
		dependientes = 2
		cuota = cotizador.calcular_cuota_basica(dependientes)
		adicional = cotizador.calcular_valores_adicionales(
			edad,
			sexo,
			estado_civil,
			especial
		)
		cotizacion = cotizador.cotizar_seguro(
			ciudad,
			edad,
			sexo,
			estado_civil,
			especial,
			dependientes
		)
		resultado_esperado = "El valor calculado de su cotización es de 110.00"
		self.assertEqual(cotizacion, resultado_esperado)

	def test_cotizador_CP3(self):
		ciudad = 'Guayaquil'
		edad = 25
		sexo = 'mujer'
		estado_civil = 'casado'
		especial = None
		dependientes = 3
		cuota = cotizador.calcular_cuota_basica(dependientes)
		adicional = cotizador.calcular_valores_adicionales(
			edad,
			sexo,
			estado_civil,
			especial
		)
		cotizacion = cotizador.cotizar_seguro(
			ciudad,
			edad,
			sexo,
			estado_civil,
			especial,
			dependientes
		)
		resultado_esperado = "El valor calculado de su cotización es de 120.00"
		self.assertEqual(cotizacion, resultado_esperado)

	def test_cotizador_CP4(self):
		ciudad = 'Guayaquil'
		edad = 25
		sexo = 'mujer'
		estado_civil = 'casado'
		especial = None
		dependientes = 4
		cuota = cotizador.calcular_cuota_basica(dependientes)
		adicional = cotizador.calcular_valores_adicionales(
			edad,
			sexo,
			estado_civil,
			especial
		)
		cotizacion = cotizador.cotizar_seguro(
			ciudad,
			edad,
			sexo,
			estado_civil,
			especial,
			dependientes
		)
		resultado_esperado = "El valor calculado de su cotización es de 140.00"
		self.assertEqual(cotizacion, resultado_esperado)

	def test_cotizador_CP5(self):
		ciudad = 'Quito'
		edad = 25
		sexo = 'mujer'
		estado_civil = 'soltero'
		especial = None
		dependientes = 0
		cuota = cotizador.calcular_cuota_basica(dependientes)
		adicional = cotizador.calcular_valores_adicionales(
			edad,
			sexo,
			estado_civil,
			especial
		)
		cotizacion = cotizador.cotizar_seguro(
			ciudad,
			edad,
			sexo,
			estado_civil,
			especial,
			dependientes
		)
		resultado_esperado = "El valor calculado de su cotización es de 40.00"
		self.assertEqual(cotizacion, resultado_esperado)

	def test_cotizador_CP6(self):
		ciudad = 'Quito'
		edad = 25
		sexo = 'mujer'
		estado_civil = 'soltero'
		especial = None
		dependientes = 2
		cuota = cotizador.calcular_cuota_basica(dependientes)
		adicional = cotizador.calcular_valores_adicionales(
			edad,
			sexo,
			estado_civil,
			especial
		)
		cotizacion = cotizador.cotizar_seguro(
			ciudad,
			edad,
			sexo,
			estado_civil,
			especial,
			dependientes
		)
		resultado_esperado = "El valor calculado de su cotización es de 100.00"
		self.assertEqual(cotizacion, resultado_esperado)

	def test_cotizador_CP7(self):
		ciudad = 'Quito'
		edad = 25
		sexo = 'mujer'
		estado_civil = 'divorciada'
		especial = None
		dependientes = 2
		cuota = cotizador.calcular_cuota_basica(dependientes)
		adicional = cotizador.calcular_valores_adicionales(
			edad,
			sexo,
			estado_civil,
			especial
		)
		cotizacion = cotizador.cotizar_seguro(
			ciudad,
			edad,
			sexo,
			estado_civil,
			especial,
			dependientes
		)
		resultado_esperado = "El valor calculado de su cotización es de 100.00"
		self.assertEqual(cotizacion, resultado_esperado)

	def test_cotizador_CP8(self):
		ciudad = 'Quito'
		edad = 25
		sexo = 'mujer'
		estado_civil = 'divorciada'
		especial = None
		dependientes = 5
		cuota = cotizador.calcular_cuota_basica(dependientes)
		adicional = cotizador.calcular_valores_adicionales(
			edad,
			sexo,
			estado_civil,
			especial
		)
		cotizacion = cotizador.cotizar_seguro(
			ciudad,
			edad,
			sexo,
			estado_civil,
			especial,
			dependientes
		)
		resultado_esperado = "Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud."
		self.assertEqual(cotizacion, resultado_esperado)

	def test_cotizador_CP9(self):
		ciudad = 'Portoviejo'
		edad = 25
		sexo = 'mujer'
		estado_civil = 'divorciada'
		especial = None
		dependientes = 5
		cuota = cotizador.calcular_cuota_basica(dependientes)
		adicional = cotizador.calcular_valores_adicionales(
			edad,
			sexo,
			estado_civil,
			especial
		)
		cotizacion = cotizador.cotizar_seguro(
			ciudad,
			edad,
			sexo,
			estado_civil,
			especial,
			dependientes
		)
		resultado_esperado = "Saludcita no opera en la ciudad ingresada."
		self.assertEqual(cotizacion, resultado_esperado)

	def test_cotizador_CP10(self):
		ciudad = 'Quito'
		edad = 17
		sexo = 'mujer'
		estado_civil = 'soltero'
		especial = None
		dependientes = 0
		cuota = cotizador.calcular_cuota_basica(dependientes)
		adicional = cotizador.calcular_valores_adicionales(
			edad,
			sexo,
			estado_civil,
			especial
		)
		cotizacion = cotizador.cotizar_seguro(
			ciudad,
			edad,
			sexo,
			estado_civil,
			especial,
			dependientes
		)
		resultado_esperado = "La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años."
		self.assertEqual(cotizacion, resultado_esperado)

	def test_cotizador_CP11(self):
		ciudad = 'Guayaquil'
		edad = 25
		sexo = 'hombre'
		estado_civil = 'casado'
		especial = None
		dependientes = 1
		cuota = cotizador.calcular_cuota_basica(dependientes)
		adicional = cotizador.calcular_valores_adicionales(
			edad,
			sexo,
			estado_civil,
			especial
		)
		cotizacion = cotizador.cotizar_seguro(
			ciudad,
			edad,
			sexo,
			estado_civil,
			especial,
			dependientes
		)
		resultado_esperado = "El valor calculado de su cotización es de 60.00"
		self.assertEqual(cotizacion, resultado_esperado)

	def test_cotizador_CP12(self):
		ciudad = 'Guayaquil'
		edad = 25
		sexo = 'hombre'
		estado_civil = 'casado'
		especial = None
		dependientes = 3
		cuota = cotizador.calcular_cuota_basica(dependientes)
		adicional = cotizador.calcular_valores_adicionales(
			edad,
			sexo,
			estado_civil,
			especial
		)
		cotizacion = cotizador.cotizar_seguro(
			ciudad,
			edad,
			sexo,
			estado_civil,
			especial,
			dependientes
		)
		resultado_esperado = "El valor calculado de su cotización es de 100.00"
		self.assertEqual(cotizacion, resultado_esperado)

	def test_cotizador_CP13(self):
		ciudad = 'Guayaquil'
		edad = 25
		sexo = 'hombre'
		estado_civil = 'soltero'
		especial = None
		dependientes = 0
		cuota = cotizador.calcular_cuota_basica(dependientes)
		adicional = cotizador.calcular_valores_adicionales(
			edad,
			sexo,
			estado_civil,
			especial
		)
		cotizacion = cotizador.cotizar_seguro(
			ciudad,
			edad,
			sexo,
			estado_civil,
			especial,
			dependientes
		)
		resultado_esperado = "El valor calculado de su cotización es de 70.00"
		self.assertEqual(cotizacion, resultado_esperado)

	def test_cotizador_CP14(self):
		ciudad = 'Guayaquil'
		edad = 25
		sexo = 'hombre'
		estado_civil = 'divorciada'
		especial = None
		dependientes = 5
		cuota = cotizador.calcular_cuota_basica(dependientes)
		adicional = cotizador.calcular_valores_adicionales(
			edad,
			sexo,
			estado_civil,
			especial
		)
		cotizacion = cotizador.cotizar_seguro(
			ciudad,
			edad,
			sexo,
			estado_civil,
			especial,
			dependientes
		)
		resultado_esperado = "Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud."
		self.assertEqual(cotizacion, resultado_esperado)

	def test_cotizador_CP15(self):
		ciudad = 'Portoviejo'
		edad = 25
		sexo = 'hombre'
		estado_civil = 'divorciado'
		especial = None
		dependientes = 5
		cuota = cotizador.calcular_cuota_basica(dependientes)
		adicional = cotizador.calcular_valores_adicionales(
			edad,
			sexo,
			estado_civil,
			especial
		)
		cotizacion = cotizador.cotizar_seguro(
			ciudad,
			edad,
			sexo,
			estado_civil,
			especial,
			dependientes
		)
		resultado_esperado = "Saludcita no opera en la ciudad ingresada."
		self.assertEqual(cotizacion, resultado_esperado)

	def test_cotizador_CP16(self):
		ciudad = 'Quito'
		edad = 17
		sexo = 'hombre'
		estado_civil = 'soltero'
		especial = None
		dependientes = 0
		cuota = cotizador.calcular_cuota_basica(dependientes)
		adicional = cotizador.calcular_valores_adicionales(
			edad,
			sexo,
			estado_civil,
			especial
		)
		cotizacion = cotizador.cotizar_seguro(
			ciudad,
			edad,
			sexo,
			estado_civil,
			especial,
			dependientes
		)
		resultado_esperado = "La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años."
		self.assertEqual(cotizacion, resultado_esperado)




if __name__ == '__main__':
	unittest.main()
