import unittest
from app import main

class test_sicei(unittest.TestCase):

    def test_get_students(self):
        alumnos = main.get_alumnos()
        print(type(alumnos))
        self.assertIsInstance(alumnos, list)


if __name__ == '__main__':
    unittest.main()