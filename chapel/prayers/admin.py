from django.contrib import admin
from django.utils.timezone import now
from chapel.prayers.models import Prayer


class PrayerModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'prayer')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'created_at')
    list_filter = ('created_at',)

    def lit_today(self, obj):
        return obj.created_at == now().date()

    lit_today.short_description = 'acesa hoje?'
    lit_today.boolean = True


admin.site.register(Prayer, PrayerModelAdmin)
