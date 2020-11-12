from django.test import TestCase
from chapel.prayers.models import Prayer
from chapel.prayers.forms import PrayerForm


class HomeGet(TestCase):
    def setUp(self):
        self.resp = self.client.get('')

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """MUST use index.html"""
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_html(self):
        contents = (
            ('<em>Bem-Aventurada Clélia Merloni</em>', 1),
            ('title="Faça sua prece"', 1),
            ('<li><a class="nav-button" href="https://unisagrado.edu.br/no-unisagrado/pastoral">Sobre a pastoral</a></li>', 1),
            ('title="Veja as velas acesas"', 1),
        )

        for expected, count in contents:
            with self.subTest():
                self.assertContains(self.resp, expected, count)
