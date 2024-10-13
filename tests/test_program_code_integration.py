import unittest
import sys
import os
from io import StringIO
from contextlib import redirect_stdout

#parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from programCode import main

class TestProgramCodeIntegration(unittest.TestCase):
    def test_main_output(self):
        # Capture the output of the main function
        with StringIO() as buf, redirect_stdout(buf):
            main()  # Call the main function
            output = buf.getvalue()  # Get the output
        
        # Check if the output contains the expected string
        self.assertIn("The square of 5 is 25", output)

if __name__ == "__main__":
    unittest.main()
