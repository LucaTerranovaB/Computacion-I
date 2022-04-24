import unittest
import main

#UNITTEST

class PalindromoUnittest(unittest.TestCase):

    def test_ana(self):
        self.assertEqual(main.palindromo("ana"), True)

    def test_hola(self):
        self.assertEqual(main.palindromo("hola"), False)
    
    def test_neuquen(self):
        self.assertEqual(main.palindromo("neuquen"), True)

    def test_reconocer(self):
        self.assertEqual(main.palindromo("reconocer"), True)

    def test_profesor(self):
        self.assertEqual(main.palindromo("profesor"), False)
        
    


if __name__=='__main__':
    unittest.main()
