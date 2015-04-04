# ivo.name() == "Ivo" # True
# ivo.email() == "ivo@pandamail.com"  # True
# ivo.gender() == "male" # True
# ivo.isMale() == True # True
# ivo.isFemale() == False # True

import unittest
from panda_social_network import Panda

class TestPanda(unittest.TestCase):

    def setUp(self):
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")
    
    def test_init(self):
        self.assertTrue(isinstance(self.ivo, Panda))

        with self.assertRaises(ValueError):
            not_panda = Panda("Pesho", "peshopandamail.com", "male")
        with self.assertRaises(TypeError):
            not_panda = Panda(10, "pesho@pandamail.com", "male")
        with self.assertRaises(TypeError):
            not_panda = Panda("Pesho", 0, "male")
        with self.assertRaises(TypeError):
            not_panda = Panda("Pesho", "pesho@pandamail.com", 9)

    def test_get_name(self):
        self.assertEqual(self.ivo.get_name(), "Ivo")

    def test_get_email(self):
        self.assertEqual(self.ivo.get_email(), "ivo@pandamail.com")

    def test_get_gender(self):
        self.assertEqual(self.ivo.get_gender(), "male")

    def test_isMale(self):
        self.assertTrue(self.ivo.isMale())

    def test_isFemale(self):
        self.assertFalse(self.ivo.isFemale())

    def test_str(self):
        self.assertEqual(str(self.ivo), "name: Ivo email: ivo@pandamail.com gender: male" )

    def test_eq(self):
        same_panda = Panda("Ivo", "ivo@pandamail.com", "male")
        self. assertTrue(self.ivo == same_panda)

    def test_hash(self):
        test_dict = {}
        test_dict[self.ivo] = 1
        self.assertEqual(hash(self.ivo), hash(self.ivo.get_email()))

if __name__ == '__main__':
    unittest.main()