from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):
    def test_home_page_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_content_existence(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Home page')

    def test_home_page_by_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_correct_template_used_for_home_page_view(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')



