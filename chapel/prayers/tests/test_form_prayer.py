from django.test import TestCase
from chapel.prayers.forms import PrayerForm


class PrayerFormTest(TestCase):
    def test_form_has_fields(self):
        """Form must have 3 fields"""
        form = PrayerForm()
        expected = ['name', 'email', 'description']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_name_must_be_capitalized(self):
        """Name must be capitalized"""
        form = self.make_validated_form(name='VINICIUS boscoa')
        self.assertEqual('Vinicius Boscoa', form.cleaned_data['name'])

    def make_validated_form(self, **kwargs):
        valid = dict(name='Vinicius Boscoa', email='valid@email.com',
                     description='Pelas famílias')
        data = dict(valid, **kwargs)
        form = PrayerForm(data)
        form.is_valid()
        return form
