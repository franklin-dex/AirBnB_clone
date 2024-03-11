import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up a User instance for testing"""
        self.user = User()

    def test_attributes(self):
        """Test if the User instance has the correct attributes"""
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_inheritance(self):
        """Test if User inherits from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_attribute_types(self):
        """Test if the attribute types are correct"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)


if __name__ == '__main__':
    unittest.main()
