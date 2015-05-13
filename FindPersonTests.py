import unittest
from Crowdmap import Crowdmap

class FindPersonTests(unittest.TestCase):
	def setUp(self):
		self.crowdmap = Crowdmap(["I met Or A. at Chabad house Bangkok", 
									"We found Or A. R.I.P at Langtang valley",
									"MissingCowboy",
									"Lassy Come Home"])
		
	def test_getAllPostsForName(self):
		posts = self.crowdmap.get_all_posts_for("Or")
		self.assertEquals(posts, ["I met Or A. at Chabad house Bangkok", "We found Or A. R.I.P at Langtang valley"])

	def test_getAllPostForMissingName(self):
		posts = self.crowdmap.get_all_posts_for("Joe")
		self.assertEquals([], posts)
		
	def test_existingLocationInformationReturnsTrue(self):
		location_exist = self.crowdmap.is_location_for_name("Or")
		self.assertTrue(location_exist)
		
if __name__ == '__main__':
	unittest.main()