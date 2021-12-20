import unittest
import translator

class TestNull(unittest.TestCase):

    def test_e2f(self):
        self.assertEqual(translator.english_to_french('Hello'),  "Bonjour")

    def test_f2e(self):
        self.assertEqual(translator.french_to_english('Bonjour'), "Hello")

    def test_e2f_none(self):
        self.assertIsNone(translator.english_to_french(),  "No Input Given")

    def test_f2e_none(self):
        self.assertIsNone(translator.french_to_english(), "Aucune Entree Donnee")

if __name__ == '__main__':
    unittest.main()