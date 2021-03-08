from django.urls import path
from .views import contact, send_email, subscribe_newsletter

app_name = 'contact'

urlpatterns = [
    path('', contact, name='contact'),
    path('send-email/', send_email, name='send_email'),
    path('subscribe-newsletter/', subscribe_newsletter, name='subscribe_newsletter')
]