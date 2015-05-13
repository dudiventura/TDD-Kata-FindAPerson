class Crowdmap(object):
	def __init__(self, init_list):
		self.list = init_list
	
	def get_all_posts_for(self, name):
		return [post for post in self.list if post.find(name) != -1]
		
	def is_location_for_name(self, name):
		posts = [post for post in self.list if post.find(name) != -1 and post.find('at') != -1]
		return len(posts) != 0
		
	def is_map_consistence(self, name):
		existsInMap = False
		for i in self.list:
			if i.find(name) != -1 and existsInMap:
				return False
			if i.find(name) != -1:
				existInMap = True
		
		return True 