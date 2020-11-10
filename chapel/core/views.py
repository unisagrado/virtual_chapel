from django.shortcuts import render
from chapel.core.forms import PrayersForm


def home(request):
    form = PrayersForm()
    return render(request, 'index.html', {'form': form})
