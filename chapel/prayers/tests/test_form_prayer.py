from django.test import TestCase
from chapel.prayers.forms import PrayerForm


class PrayerFormTest(TestCase):
    def test_form_has_fields(self):
        """Form must have 3 fields"""
        form = PrayerForm()
        expected = ['name', 'email', 'prayer']
        self.assertSequenceEqual(expected, list(form.fields))
