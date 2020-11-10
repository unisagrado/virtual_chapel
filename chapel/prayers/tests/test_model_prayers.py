from datetime import datetime
from django.test import TestCase
from chapel.prayers.models import Prayer


class PrayersModelTest(TestCase):
    def setUp(self):
        self.obj = Prayer.objects.create(
            name='Vinicius Boscoa',
            email='vinicius.boscoa@unisagrado.edu.br',
            prayer='Pelas famílias'
        )

    def test_create(self):
        self.assertTrue(Prayer.objects.exists())

    def test_created_at(self):
        """Prayer must have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)
