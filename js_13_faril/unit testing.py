import unittest

# Fungsi konversi suhu
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

class TestTemperatureConversion(unittest.TestCase):
    # Pengujian fungsi konversi
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40)
    
    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100)
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40)
    
    # Validasi input
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            celsius_to_fahrenheit("sebuah string")
            fahrenheit_to_celsius(None)
            celsius_to_fahrenheit([1, 2, 3])
            fahrenheit_to_celsius({})

if __name__ == '__main__':
    unittest.main()