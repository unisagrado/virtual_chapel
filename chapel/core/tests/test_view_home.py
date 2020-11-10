from django.test import TestCase


class HomeTest(TestCase):
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
            ('<li><a class="nav-button" href="#sobre">Sobre</a></li>', 1),
            ('<li><a class="nav-button" href="#prece">Faça sua Prece</a></li>', 1),
            ('<form', 1),
            ('<label', 3),
            ('<input', 3),
            ('<textarea', 1),
            ('<button', 3),
        )

        for expected, count in contents:
            with self.subTest():
                self.assertContains(self.resp, expected, count)
