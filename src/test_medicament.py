import unittest
from medicament import registrar_medicamento

class TestMedicamento(unittest.TestCase):

    def test_registrar_medicamento_exitoso(self):
        """CP-01/04: Valida el registro correcto de un medicamento valido"""
        resultado = registrar_medicamento("Paracetamol 500mg", 100, 2.50)
        self.assertTrue(resultado["exito"])
        self.assertEqual(resultado["medicamento"]["nombre"], "Paracetamol 500mg")

    def test_precio_negativo_falla(self):
        """CP-01: Valida que no se permitan precios negativos"""
        resultado = registrar_medicamento("Ibuprofeno", 50, -5.00)
        self.assertFalse(resultado["exito"])
        self.assertEqual(resultado["error"], "El precio debe ser mayor a cero")

if __name__ == '__main__':
    unittest.main()