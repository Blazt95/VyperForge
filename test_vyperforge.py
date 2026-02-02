# test_vyperforge.py
"""
Tests for VyperForge module.
"""

import unittest
from vyperforge import VyperForge

class TestVyperForge(unittest.TestCase):
    """Test cases for VyperForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VyperForge()
        self.assertIsInstance(instance, VyperForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VyperForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
