from django.forms.widgets import Textarea
from chapel.prayers.models import Prayer
from django import forms


class PrayerForm(forms.ModelForm):
    class Meta:
        model = Prayer
        fields = ['name', 'email', 'description']
        widgets = {
            'description': Textarea(attrs={'rows': 5})
        }
        labels = {
            'description': 'Deixe sua prece'
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)
