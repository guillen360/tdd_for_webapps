
# function test cases--> tests from your user point of view

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.home_page = 'http://localhost:8000'

	def tearDown(self):
		self.browser.quit()
		# self.browser.implicitly_wait(3)

	def test_starting_a_todo_list(self):
		self.browser.get(self.home_page)

		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)		

		# enter a to-do item:
			#first verify input box:
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

		# when page submits, page updates and page lists:
		inputbox.send_keys('Buy Peacock feather')
		inputbox.send_keys(Keys.ENTER)

		# page update, we expect to see data entered:
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		# self.assertTrue(any(row.text == '1: Buy Peacock feather' for row in rows))

		self.assertIn('1: Buy Peacock feather', [row.text for row in rows])

		# there is still a text box inviting her to add another item
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
		inputbox.send_keys('User peacock feather to make fly')
		inputbox.send_keys(Keys.ENTER)		

		# page updates again
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')		

		self.assertIn('2: User peacock feather to make fly', [row.text for row in rows])
		self.assertIn('1: Buy Peacock feather', [row.text for row in rows])
		# # hit refresh
			
		# test are not complete yet...
		self.fail('finish writing the test!')
if __name__ == '__main__':
	unittest.main()
