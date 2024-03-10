import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Set up a City instance for testing"""
        self.city = City()

    def test_attributes(self):
        """Test if the City instance has the correct attributes"""
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_inheritance(self):
        """Test if City inherits from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attribute_types(self):
        """Test if the attribute types are correct"""
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

if __name__ == '__main__':
    unittest.main()

