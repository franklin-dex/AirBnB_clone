import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        """Set up a Review instance for testing."""
        self.review = Review()

    def test_attributes_initialization(self):
        """Test if the attributes are initialized properly."""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_attributes_update(self):
        """Test if the attributes can be updated properly."""
        self.review.place_id = "123"
        self.review.user_id = "456"
        self.review.text = "Great place!"

        self.assertEqual(self.review.place_id, "123")
        self.assertEqual(self.review.user_id, "456")
        self.assertEqual(self.review.text, "Great place!")

    # Add more test cases as needed...


if __name__ == '__main__':
    unittest.main(i)
