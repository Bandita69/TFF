# Import the whole unittest module.
import unittest
# Import DonorData class from the Donor file.
from Donor import DonorData


# Create definitions for each test case in the DonorTests class.
class DonorTests(unittest.TestCase):
    def test_get_sickness(self):
        self.assertEqual("Y", DonorData.get_sickness(self), "The answer should be Y or N.")

if __name__ == '__main__':
    unittest.main()
