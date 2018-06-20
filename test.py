# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from cotizador import cotizar_seguro

class Test(unittest.TestCase):
    ##Reemplace ID por el número identificador que utilizó en la plantilla de pruebas.
    def test_cotizador_cp001(self):
        resultado = cotizar_seguro('Guayaquil',40, 'mujer', 'casado', '', 0)
        self.assertEqual(resultado, "El valor calculado de su cotización es de 50.00")

    def test_cotizador_cp002(self):
        resultado = cotizar_seguro('Quito', 30, 'hombre', 'soltero', '', 0)
        self.assertEqual(resultado, "El valor calculado de su cotización es de 70.00")

    def test_cotizador_cp003(self):
        resultado = cotizar_seguro('Guayaquil', 40, 'mujer', 'soltero', '', 3)
        self.assertEqual(resultado, "El valor calculado de su cotización es de 110.00")

    def test_cotizador_cp004(self):
        resultado = cotizar_seguro('Guayaquil', 40, 'mujer', 'casado', '', 5)
        self.assertEqual(resultado, "Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud.")

    def test_cotizador_cp005(self):
        resultado = cotizar_seguro('Guayaquil', 40, 'mujer', 'casado', 'osteoporosis', 0)
        self.assertEqual(resultado, "El valor calculado de su cotización es de 50.00")

    def test_cotizador_cp006(self):
        resultado = cotizar_seguro('Quito', 30, 'hombre', 'soltero', 'cancer', 0)
        self.assertEqual(resultado, "El valor calculado de su cotización es de 70.00")

    def test_cotizador_cp007(self):
        resultado = cotizar_seguro('Guayaquil', 40, 'mujer', 'soltero', 'osteoporosis', 3)
        self.assertEqual(resultado, "El valor calculado de su cotización es de 110.00")

    def test_cotizador_cp008(self):
        resultado = cotizar_seguro('Guayaquil', 40, 'mujer', 'casado', 'diabetes', 5)
        self.assertEqual(resultado, "Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud.")
if __name__ == '__main__':
	unittest.main()
