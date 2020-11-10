from django.test import TestCase
from chapel.core.forms import PrayersForm


class PrayersFormTest(TestCase):
    def test_form_has_fields(self):
        """Form must have 3 fields"""
        form = PrayersForm()
        expected = ['name', 'email', 'prayer']
        self.assertSequenceEqual(expected, list(form.fields))
