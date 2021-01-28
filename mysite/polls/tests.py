import unittest
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from . views import index

# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, world. You\'re at the polls index.', html)

        