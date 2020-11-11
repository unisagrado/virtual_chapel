from django import forms


class PrayerForm(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email')
    description = forms.CharField(label='Deixe sua prece',
                                  widget=forms.Textarea(attrs={'rows': '5'}))

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)
