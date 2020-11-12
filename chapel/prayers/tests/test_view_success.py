from django.test import TestCase
from django.shortcuts import resolve_url as r


class PrayerSuccessGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('prayers:success'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'prayers/success.html')

    def test_html(self):
        contents = [
            'A Bem-Aventurada Clélia Merloni interceda por você e por suas intenções.',
            '<div class="success-message"',
            'Clique aqui para acender sua vela'
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected)
