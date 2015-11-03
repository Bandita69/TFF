import unittest
from Donor import DonorData


class DonorTests(unittest.TestCase):
    def test_weight(self):
        self.assertEqual(51, DonorData.i_need_your_kg(51), "A donor sulya nem lehet kevesebb mint 50 kg.")

if __name__ == '__main__':
    unittest.main()
# egyelore ez az en tesztem, de meg nem mokidik sajnos es nem ertem miert :(