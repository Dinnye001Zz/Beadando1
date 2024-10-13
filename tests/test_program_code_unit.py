import unittest
import sys
import os

#parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from programCode import square

class TestProgramCode(unittest.TestCase):
    def test_square(self):
        # Test cases for the square function
        self.assertEqual(square(2), 4)      # 2 squared is 4
        self.assertEqual(square(-3), 9)     # -3 squared is 9
        self.assertEqual(square(0), 0)      # 0 squared is 0
        self.assertEqual(square(1.5), 2.25)  # 1.5 squared is 2.25

if __name__ == "__main__":
    unittest.main()