from django.test import TestCase, Client

# Create your tests here.
class TestView(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_main_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)