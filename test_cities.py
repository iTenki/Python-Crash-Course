import unittest
from city_functions import get_locations

class CityTestCase(unittest.TestCase):
	def test_city_country(self):
		location = get_locations('santiage', 'chile')
		self.assertEqual(location, 'Santiage, Chile')

unittest.main()