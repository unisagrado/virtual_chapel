from django.urls import path
from chapel.prayers.views import new, success, listing

app_name = 'prayers'

urlpatterns = [
    path('acender-vela/', new, name='new'),
    path('sucesso/', success, name='success'),
    path('velas-acesas/', listing, name='list')
]
