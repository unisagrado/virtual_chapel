from django.urls import path
from chapel.prayers.views import new, success

app_name = 'prayers'

urlpatterns = [
    path('', new, name='new'),
    path('success/', success, name='success')
]
