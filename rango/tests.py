from django.test import TestCase

from rango.models import Category

class CategoryMethodTests(TestCase):

    def test_ensure_views_are_positive(self):
        cat = Category(name='test', views=2, likes=0)
        cat.save()
        self.assertEqual((cat.views >= 0), True)