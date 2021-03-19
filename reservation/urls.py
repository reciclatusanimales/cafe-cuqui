from django.urls import path
from .views import reserve_table, reserve


app_name = 'reservation'

urlpatterns = [
    path('', reserve_table, name='reserve_table'),
    path('reserve/', reserve, name='reserve'),
]