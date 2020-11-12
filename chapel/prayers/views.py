from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, resolve_url as r
from chapel.prayers.forms import PrayerForm
from chapel.prayers.models import Prayer


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'prayers/prayer_form.html', {'form': PrayerForm()})


def create(request):
    form = PrayerForm(request.POST)
    if not form.is_valid():
        return render(request, 'prayers/prayer_form.html', {'form': form})

    form.save()
    return HttpResponseRedirect(r('prayers:success'))


def success(request):
    return render(request, 'prayers/success.html')


def listing(request):
    context = {'prayers': Prayer.objects.lit_candles().order_by('-created_at')}
    return render(request, 'prayers/list.html', context)
