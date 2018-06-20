# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import cotizador

class Test(unittest.TestCase):
    def test_cotizador_1(self)
        self.assertEqual("El valor es de 60.00",cotizador.cotizar_seguro("Cuenca",35, "hombre", "casado", "",0))

    def test_cotizador_2(self)
        self.assertEqual("El valor es de 70.00",cotizador.cotizar_seguro("Cuenca",35, "hombre", "soltero", "",0))	

    def test_cotizador_3(self)
        self.assertEqual("El valor es de 0.00",cotizador.cotizar_seguro("Cuenca",16, "hombre", "soltero", "",0))	

    def test_cotizador_4(self)
        self.assertEqual("El valor es de 80.00",cotizador.cotizar_seguro("Guayaquil",18, "mujer", "casado", "",0))

    def test_cotizador_5(self)
        self.assertEqual("El valor es de 40.00",cotizador.cotizar_seguro("Guayaquil",18, "mujer", "soltero", "",0))	

    def test_cotizador_6(self)
        self.assertEqual("El valor es de 0.00",cotizador.cotizar_seguro("Guayaquil",16, "mujer", "soltero", "",0))

    def test_cotizador_7(self)
        self.assertEqual("El valor es de 130.00",cotizador.cotizar_seguro("Cuenca",35, "hombre", "soltero", "",2))

    def test_cotizador_8(self)
        self.assertEqual("El valor es de 120.00",cotizador.cotizar_seguro("Guayaquil",18, "mujer", "casado", "",3))		
	

if __name__ == '__main__':
	unittest.main()