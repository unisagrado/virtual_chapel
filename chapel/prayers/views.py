from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, resolve_url as r
from chapel.prayers.forms import PrayerForm
from chapel.prayers.models import Prayer


def new(request):
    if request.method == 'POST':
        form = PrayerForm(request.POST)
        if not form.is_valid():
            return render(request, 'prayers/prayer_form.html', {'form': form})

        Prayer.objects.create(**form.cleaned_data)
        return HttpResponseRedirect(r('prayers:success'))

    form = PrayerForm()
    return render(request, 'prayers/prayer_form.html', {'form': PrayerForm()})


def success(request):
    return render(request, 'prayers/success.html')
