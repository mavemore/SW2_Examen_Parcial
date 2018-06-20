# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import cotizador

class Test(unittest.TestCase):
	#Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.
	def test_cotizador_1(self):
                total = cotizador.cotizar_seguro('Guayaquil',20,'mujer','casado','ninguno',1)
                self.assertEqual(total,'El valor calculado de su cotización es de 80.00')

        def test_cotizador_2(self):
                total = cotizador.cotizar_seguro('Cuenca',20,'mujer','casado','ninguno',2)
                self.assertEqual(total,'El valor calculado de su cotización es de 110.00')

        def test_cotizador_3(self):
                total = cotizador.cotizar_seguro('Machala',20,'mujer','casado','ninguno',3)
                self.assertEqual(total,'El valor calculado de su cotización es de 120.00')

        def test_cotizador_4(self):
                total = cotizador.cotizar_seguro('Quito',20,'mujer','soltero','ninguno',0)
                self.assertEqual(total,'El valor calculado de su cotización es de 40.00')

        def test_cotizador_6(self):
                total = cotizador.cotizar_seguro('Quito',20,'mujer','divorciado','ninguno',1)
                self.assertEqual(total,'El valor calculado de su cotización es de 70.00')

        def test_cotizador_8(self):
                total = cotizador.cotizar_seguro('Guayaquil',20,'mujer','viudo','ninguno',3)
                self.assertEqual(total,'El valor calculado de su cotización es de 110.00')

        def test_cotizador_10(self):
                total = cotizador.cotizar_seguro('Guayaquil',18,'hombre','soltero','ninguno',0)
                self.assertEqual(total,'El valor calculado de su cotización es de 70.00')

        def test_cotizador_11(self):
                total = cotizador.cotizar_seguro('Guayaquil',20,'hombre','casado','ninguno',1)
                self.assertEqual(total,'El valor calculado de su cotización es de 60.00')


if __name__ == '__main__':
	unittest.main()