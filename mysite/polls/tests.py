import unittest
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from . views import index
from . models import Question, Choice

# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, world. You\'re at the polls index.', html)


    def test_saving_and_retrieving_items(self):
        first_question = Question()
        first_question.question_text = 'What is your favorite color?'
        first_question.save()

        second_question = Question()
        second_question.question_text = 'What is the best day of the week?'
        second_question.save()

        saved_items = Question.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_question = saved_items[0]
        second_saved_question = saved_items[1]
        self.assertEqual(first_saved_question.question_text, 'What is your favorite color?')
        self.assertEqual(second_saved_question.question_text, 'What is the best day of the week?')