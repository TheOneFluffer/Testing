import unittest
import myProgram as prog

#Part 1
class TestMyProgram(unittest.TestCase):

    def test_EngineType(self):
        print("Testing")

if __name__ == '__main__':
    unittest.main()

#Part 2
class TestMyProgram(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

#Part 3
class TestMyProgram(unittest.TestCase):
    def test_EngineType(self):
        vios = prog.Vehicle('4', 'petrol', 5, 180)
        self.assertEqual(vios.type_of_tank, 'petrol')

if __name__ == '__main__':
    unittest.main()