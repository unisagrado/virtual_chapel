from django import forms


class PrayersForm(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email')
    prayer = forms.CharField(label='Deixe sua prece',
                             widget=forms.Textarea(attrs={'rows': '5'}))
