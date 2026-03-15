# test_argocdgitops.py
"""
Tests for ArgoCdGitops module.
"""

import unittest
from argocdgitops import ArgoCdGitops

class TestArgoCdGitops(unittest.TestCase):
    """Test cases for ArgoCdGitops class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArgoCdGitops()
        self.assertIsInstance(instance, ArgoCdGitops)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArgoCdGitops()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
