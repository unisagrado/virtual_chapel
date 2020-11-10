from django.test import TestCase
from django.shortcuts import resolve_url as r
from chapel.prayers.models import Prayer
from chapel.prayers.forms import PrayerForm


class PrayersNewGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('prayers:new'))

    def test_get(self):
        """Get /faca-sua-prece/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """ Must use prayers/prayers_form.html"""
        self.assertTemplateUsed(self.resp, 'prayers/prayer_form.html')

    def test_html(self):
        """HTML must contain input tags"""
        tags = (
            ('<form', 1),
            ('<label', 3),
            ('<input', 3),
            ('<textarea', 1),
            ('type="text"', 1),
            ('type="email"', 1),
        )

        for expected, count in tags:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    def test_csrf(self):
        """HTML must contains csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have prayer form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, PrayerForm)


class PrayersNewPostValid(TestCase):
    def setUp(self):
        data = dict(name='Vinicius Boscoa', email='vinicius.boscoa@unisagrado.edu.br',
                    prayer='Pelas famílias')
        self.resp = self.client.post(r('prayers:new'), data)

    def test_post(self):
        """Valid POST should redirect to /sucesso/"""
        self.assertEqual(302, self.resp.status_code)

    def test_save_prayer(self):
        self.assertTrue(Prayer.objects.exists())


class PrayersNewPostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('prayers:new'), {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'prayers/prayer_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, PrayerForm)

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_prayer(self):
        self.assertFalse(Prayer.objects.exists())
