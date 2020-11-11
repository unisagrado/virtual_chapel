from datetime import datetime
from django.utils import timezone
from django.test import TestCase
from chapel.prayers.models import Prayer
from chapel.prayers.managers import LitManager


class PrayerModelTest(TestCase):
    def setUp(self):
        self.obj = Prayer.objects.create(
            name='Vinicius Boscoa',
            email='valid@email.com',
            description='Pelas famílias'
        )

    def test_create(self):
        self.assertTrue(Prayer.objects.exists())

    def test_created_at(self):
        """Prayer must have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Vinicius Boscoa', str(self.obj))


class LitManagerTest(TestCase):
    def setUp(self):
        SUBTRACT_DAYS = 8
        date_7days_before = timezone.now() - timezone.timedelta(days=SUBTRACT_DAYS)
        p1 = Prayer.objects.create(name='Vinicius', email='valid@email.com',
                                   description='Vela acesa')
        p2 = Prayer.objects.create(name='Vinicius', email='valid@email.com',
                                   description='Vela apagada')
        p2.created_at = date_7days_before
        p2.save()

    def test_manager(self):
        self.assertIsInstance(Prayer.objects, LitManager)

    def test_lit_candle(self):
        qs = Prayer.objects.lit_candles()
        expected = ['Vela acesa']
        self.assertQuerysetEqual(qs, expected, lambda o: o.description)
