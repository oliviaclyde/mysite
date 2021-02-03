import unittest
from django.test import TestCase, Client, RequestFactory
from django.http import HttpRequest, HttpResponse
from django.template.loader import render_to_string
from . views import index, detail
from . models import Question, Choice
from django.urls import reverse


# Create your tests here.
class HomePageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_home_page_returns_correct_html(self):
        request = self.factory.get('/polls/index')
        response = index(request)
        self.assertEqual(response.status_code, 200)
        # response = self.client.get('/')
        # self.assertTemplateUsed(response, 'index.html')

    # def test_no_entries(self):
    #     response = self.client.get('/')
    #     self.assertContains(response, 'No blog entires yet.')

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


def create_question(question_text):
        return Question.objects.create(question_text=question_text)

class ViewsTest(TestCase):
    # def get_request(self):
    #     request = HttpRequest()
    #     first_question = Question()
    #     question_id = first_question.question_text("Is this your question?")
    #     # question_id = 1
    #     return request
    
    def test_detail(self):    
        first_question = create_question(question_text="Is this your question?")
        url = reverse('polls:detail', args=(first_question.id,))
        response = self.client.get(url)
        self.assertContains(response, first_question.question_text)
        
    def test_results(self):
        pass

    def vote(self):
        pass