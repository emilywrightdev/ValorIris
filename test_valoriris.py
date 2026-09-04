# test_valoriris.py
"""
Tests for ValorIris module.
"""

import unittest
from valoriris import ValorIris

class TestValorIris(unittest.TestCase):
    """Test cases for ValorIris class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ValorIris()
        self.assertIsInstance(instance, ValorIris)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ValorIris()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
