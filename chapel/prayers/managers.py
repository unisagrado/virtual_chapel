from django.utils import timezone
from django.db import models


class LitManager(models.Manager):
    DAYS_LIMIT = 7

    def lit_candles(self):
        last_week = timezone.now() - timezone.timedelta(days=self.DAYS_LIMIT)
        return self.filter(created_at__gte=last_week)
