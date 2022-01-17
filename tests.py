import unittest
from program import Program

class TestProgram(unittest.TestCase):
    def setUp(self):
        file_name = 'file.txt'
        self.prog = Program(file_name)

    def test_add(self):
        self.assertEqual(self.prog.add(), 10)

    def test_multiply(self):
        self.assertEqual(self.prog.multiply(), 24)

    def test_find_min(self):
        self.assertEqual(self.prog.find_min(), 1)

    def test_find_max(self):
        self.assertEqual(self.prog.find_max(), 4)

    def test_file_exists(self):
        self.assertTrue(self.prog.file_exists('file.txt'))
        self.assertFalse(self.prog.file_exists('file2.txt'))    
    def test_time_check(self):
        self.assertTrue(self.prog.time_check())
if __name__ == "__main__":
    unittest.main()