import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def setUp(self):
        """Set up a State instance for testing"""
        self.state = State()

    def test_attributes(self):
        """Test if the State instance has the correct attributes"""
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))
        self.assertTrue(hasattr(self.state, 'name'))

    def test_inheritance(self):
        """Test if State inherits from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_attribute_types(self):
        """Test if the attribute types are correct"""
        self.assertIsInstance(self.state.name, str)

if __name__ == '__main__':
    unittest.main()

