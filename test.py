# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import cotizador

class Test(unittest.TestCase):
        #Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.
        def test_cotizador_1(self):
                total = cotizador.cotizar_seguro('Machala',23,'mujer','casado','ninguno',1)
                self.assertEqual(total,'El valor calculado de su cotización es de 80.00')

        def test_cotizador_2(self):
                total = cotizador.cotizar_seguro('Machala',23,'mujer','casado','ninguno',2)
                self.assertEqual(total,'El valor calculado de su cotización es de 110.00')

        def test_cotizador_3(self):
                total = cotizador.cotizar_seguro('Machala',23,'mujer','casado','ninguno',3)
                self.assertEqual(total,'El valor calculado de su cotización es de 120.00')

        def test_cotizador_4(self):
                total = cotizador.cotizar_seguro('Machala',23,'mujer','casado','ninguno',4)
                self.assertEqual(total,'El valor calculado de su cotización es de 140.00')

        def test_cotizador_5(self):
                total = cotizador.cotizar_seguro('Guayaquil',37,'mujer','soltero','ninguno',0)
                self.assertEqual(total,'El valor calculado de su cotización es de 40.00')

        def test_cotizador_6(self):
                total = cotizador.cotizar_seguro('Guayaquil',37,'mujer','divorciado','ninguno',1)
                self.assertEqual(total,'El valor calculado de su cotización es de 70.00')

        def test_cotizador_7(self):
                total = cotizador.cotizar_seguro('Guayaquil',37,'mujer','divorciado','ninguno',2)
                self.assertEqual(total,'El valor calculado de su cotización es de 100.00')

        def test_cotizador_8(self):
                total = cotizador.cotizar_seguro('Guayaquil',37,'mujer','viudo','ninguno',3)
                self.assertEqual(total,'El valor calculado de su cotización es de 110.00')

        def test_cotizador_9(self):
                total = cotizador.cotizar_seguro('Guayaquil',37,'mujer','viudo','ninguno',4)
                self.assertEqual(total,'El valor calculado de su cotización es de 130.00')

        def test_cotizador_10(self):
                total = cotizador.cotizar_seguro('Quito',18,'hombre','soltero','ninguno',0)
                self.assertEqual(total,'El valor calculado de su cotización es de 70.00')

        def test_cotizador_11(self):
                total = cotizador.cotizar_seguro('Quito',40,'hombre','casado','ninguno',1)
                self.assertEqual(total,'El valor calculado de su cotización es de 60.00')

        def test_cotizador_12(self):
                total = cotizador.cotizar_seguro('Quito',40,'hombre','divorciado','ninguno',2)
                self.assertEqual(total,'El valor calculado de su cotización es de 90.00')

        def test_cotizador_13(self):
                total = cotizador.cotizar_seguro('Quito',40,'hombre','divorciado','ninguno',3)
                self.assertEqual(total,'El valor calculado de su cotización es de 100.00')

        def test_cotizador_14(self):
                total = cotizador.cotizar_seguro('Quito',40,'hombre','viudo','ninguno',4)
                self.assertEqual(total,'El valor calculado de su cotización es de 120.00')

        def test_cotizador_15(self):
                total = cotizador.cotizar_seguro('Quito',40,'hombre','viudo','ninguno',0)
                self.assertEqual(total,'El valor calculado de su cotización es de 30.00')

        def test_cotizador_16(self):
                total = cotizador.cotizar_seguro('Quito',23,'hombre','soltero','ninguno',1)
                self.assertEqual(total,'El valor calculado de su cotización es de 100.00')

        def test_cotizador_17(self):
                total = cotizador.cotizar_seguro('Quito',27,'hombre','soltero','ninguno',2)
                self.assertEqual(total,'El valor calculado de su cotización es de 130.00')

        def test_cotizador_18(self):
                total = cotizador.cotizar_seguro('Quito',27,'hombre','soltero','ninguno',3)
                self.assertEqual(total,'El valor calculado de su cotización es de 140.00')

        def test_cotizador_19(self):
                total = cotizador.cotizar_seguro('Quito',27,'hombre','soltero','ninguno',4)
                self.assertEqual(total,'El valor calculado de su cotización es de 160.00')

        def test_cotizador_20(self):
                total = cotizador.cotizar_seguro('Quito',27,'hombre','soltero','ninguno',6)
                self.assertEqual(total,'Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud.')

        def test_cotizador_21(self):
                total = cotizador.cotizar_seguro('Manta',27,'hombre','soltero','ninguno',2)
                self.assertEqual(total,'Saludcita no opera en la ciudad ingresada.')
        

if __name__ == '__main__':
        unittest.main()
