from django.test import TestCase
from django.shortcuts import resolve_url as r
from chapel.prayers.models import Prayer


class PrayerListGet(TestCase):
    def setUp(self):
        self.p1 = Prayer.objects.create(name='Vinicius', email='valid@email.com',
                                        description='Pelas famílias')
        self.p2 = Prayer.objects.create(name='Diego', email='valid@email.com',
                                        description='Pela pastoral')

        self.resp = self.client.get(r('prayers:list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use prayers/detail.html"""
        self.assertTemplateUsed(self.resp, 'prayers/list.html')

    def test_html(self):
        """Must list registered prayers"""
        contents = [
            'Pelas famílias',
            'Pela pastoral'
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_context(self):
        """Context must contain prayers variable"""
        variable = 'prayers'
        self.assertIn(variable, self.resp.context)
