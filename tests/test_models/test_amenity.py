import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up an Amenity instance for testing"""
        self.amenity = Amenity()

    def test_attributes(self):
        """Test if the Amenity instance has the correct attributes"""
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_inheritance(self):
        """Test if Amenity inherits from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attribute_types(self):
        """Test if the attribute types are correct"""
        self.assertIsInstance(self.amenity.name, str)


if __name__ == '__main__':
    unittest.main()
