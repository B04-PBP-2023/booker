from django.test import Client, TestCase

# Create your tests here.
from django.urls import reverse
from bookshelf.models import Book

class BookshelfTestCase(TestCase):
    def setUp(self):
        # Create some sample data for testing
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            genre='Non Fiction',
            purchase_date='2023-01-01',
            due_date='2023-02-01',
            borrowed=True
        )

    def test_return_book_view(self):
        # Test if the return_book view returns a 302 (redirect) status code
        response = self.client.post(reverse('return_book', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)

        # Verify that the book's borrowed status is set to False after returning
        self.book.refresh_from_db()
        self.assertFalse(self.book.borrowed)
    
    def test_main_url_is_exist(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/')
        self.assertTemplateUsed(response, 'frontpage.html')