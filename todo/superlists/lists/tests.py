# tests from a programmers point of view

from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page
from django.template.loader import render_to_string

# Create your tests here.
class HomePageViewTest(TestCase):

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)

		self.assertTrue(response.content.startswith(b'<html>')) # b is for bits
		self.assertIn(b'<title>To-Do Lists</title>', response.content)
		self.assertTrue(response.content.strip().endswith(b'</html>'))

	def test_home_page_uses_home_template(self):
		request = HttpRequest()
		response = home_page(request)

		expected_html = render_to_string('home.html')
		self.assertEqual(response.content, expected_html)

	def test_home_page_can_handle_post_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'a new item'
		response = home_page(request)

		self.assertIn('a new item', response.content)

		expected_html = render_to_string('home.html', {'new_item_text': 'a new item' })
		self.assertEqual(response.content, expected_html)
