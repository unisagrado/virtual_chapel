from django.utils import timezone
from django.test import TestCase
from django.shortcuts import resolve_url as r
from chapel.prayers.models import Prayer


class PrayerListGet(TestCase):
    def setUp(self):
        self.p1 = Prayer.objects.create(name='Vinicius', email='valid@email.com',
                                        description='Pelas famílias')
        self.p2 = Prayer.objects.create(name='Diego', email='valid@email.com',
                                        description='Pela pastoral')

        p3 = Prayer.objects.create(name='Diego', email='valid@email.com',
                                   description='Vela apagada')

        p3.created_at = timezone.now() - timezone.timedelta(days=8)
        p3.save()

        self.resp = self.client.get(r('prayers:list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use prayers/detail.html"""
        self.assertTemplateUsed(self.resp, 'prayers/list.html')

    def test_html(self):
        """Must list lit candles"""
        contents = (
            ('Diego', 1),
            ('Vinicius', 1),
            ('Pelas famílias', 1),
            ('Pela pastoral', 1),
            ('Vela apagada', 0)
        )
        for expected, count in contents:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    def test_context(self):
        """Context must contain prayers variable"""
        variable = 'prayers'
        self.assertIn(variable, self.resp.context)


class PrayerListEmptyGet(TestCase):
    def test_get_empty(self):
        response = self.client.get(r('prayers:list'))
        self.assertContains(response, 'Não há nenhuma vela acesa')
        self.assertContains(response, 'Acenda uma vela')
