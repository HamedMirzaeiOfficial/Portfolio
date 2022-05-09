from django.test import TestCase, Client
from .models import Category
from django.conf import settings


# model test
class TestCategoryModel(TestCase):
    """Test the Category model."""
    def setUp(self):
        self.c = Category(name='sport')

    def test_create_category(self):
        self.assertIsInstance(self.c, Category)

    def test_str_representation(self):
        self.assertEqual(str(self.c), 'sport')


# view test
class TestHomeView(TestCase):
    """Test the home view."""
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)


class TestDjangoSettings(TestCase):

    def test_django_conf(self):
        """
        Check that `blog` is in `settings.INSTALLED_APPS` and that the static dir is set to <projectdir>/static.
        STATIC_ROOT and STATICFILES_STORAGE should not be set.
        """
        self.assertIn('blog.apps.BlogConfig', settings.INSTALLED_APPS)
        self.assertIsNone(settings.STATIC_ROOT)
        self.assertEqual(settings.STATICFILES_STORAGE, 'django.contrib.staticfiles.storage.StaticFilesStorage')
