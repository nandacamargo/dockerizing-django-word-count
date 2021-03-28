from django.test import TestCase
from django.urls import reverse
from . import views
from . import apps
from . import settings

class WordCountTestCase(TestCase):

   #Testing views
   def test_views_read_file(self):
      result = views.read_file('../media/test_file01.txt')

      self.assertIsNotNone(result)
      self.assertEquals(result, ['This is an example for test.\n'])

   def test_views_read_empty_file(self):
      result = views.read_file('../media/test_file02.txt')

      self.assertIsNotNone(result)
      self.assertEquals(result, [])

   #Testing apps
   def test_apps(self):
      self.assertEqual(apps.MyappConfig.name, 'mywordcount')

   #Testing settings   
   def test_settings_root_urlconf(self):
      self.assertEqual(settings.ROOT_URLCONF, 'mywordcount.urls')
   
   def test_settings_media_url(self):
      self.assertEqual(settings.MEDIA_URL, '/media/')
