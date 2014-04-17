
# test 1:
#   is the hello world page up

import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.home_page = 'http://localhost:8000'

	def tearDown(self):
		self.browser.quit()
		self.browser.implicitly_wait(3)

	def test_starting_a_todo_list(self):
		self.browser.get(self.home_page)

		self.assertIn('To-Do', self.browser.title)

# enter a to-do item:

# when page submits, page updates and page lists:

# there is still a text box inviting her to add another item

# page updates again

# hit refresh

if __name__ == '__main__':
	unittest.main()
