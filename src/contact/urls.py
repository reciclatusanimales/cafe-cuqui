from django.urls import path
from .views import contact, success

app_name = 'contact'

urlpatterns = [
    path('', contact, name='contact'),
    path('success/', success, name='success'),
]